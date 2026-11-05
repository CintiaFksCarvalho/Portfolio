import pandas as pd
import os
from tkinter import filedialog, messagebox
import tkinter as tk
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.series import SeriesLabel
from openpyxl.chart.label import DataLabelList
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

import sys

if getattr(sys, 'frozen', False):
    diretorio_atual = os.path.dirname(sys.executable)
else:
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

CAMINHO_REFERENCIAS = os.path.join(diretorio_atual, "referencias.xlsx")

# =============================================================================
# LISTA FIXA DE UPs
# =============================================================================
UPS_FIXOS = [
    "UP_A",
    "UP_B",
    "UP_C",
    "UP_D",
    "UP_E",
    "UP_F",
    "UP_G",
    "UP_H",
]

# =============================================================================
# COLUNAS MAYA — Sheet1 (64 colunas)
# =============================================================================
COLUNAS_MAYA = [
    "SITE", "DATE", "OPERATION", "QUI?", "UP", "ARTICLE", "PROVENANCE", "GOMMETTE",
    "QTE", "BONNES", "PNC", "PAD", "BPC", "DEBUT", "DUREE", "CADENCE", "METHODE",
    "PNC Ponto de suspenção", "PNC Rebarba", "PNC Branco Localizado", "PNC Bolha",
    "PNC Pancada", "PNC Zona descoberta", "PNC Deformação", "PNC Dimensional NC",
    "PNC Escama", "PNC Fibra / Matéria NC", "PNC Fissura", "PNC Funcional NC",
    "PNC Greta", "PNC Palha/Cometa", "PNC Acabamento / Gravação NC", "PNC Risco",
    "PNC Marca de usinagem", "PNC Mancha / Oxidação", "PNC Baço", "PNC Buraco",
    "PNC Buraco / Pico", "PNC Vibrado", "PNC Retoque", "PAD Ponto de suspenção",
    "PAD Rebarba", "PAD Branco Localizado", "PAD Bolha", "PAD Pancada",
    "PAD Zona descoberta", "PAD Deformação", "PAD Dimensional NC", "PAD Escama",
    "PAD Fibra / Matéria NC", "PAD Fissura", "PAD Funcional NC", "PAD Greta",
    "PAD Palha/Cometa", "PAD Acabamento / Gravação NC", "PAD Risco",
    "PAD Marca de usinagem", "PAD Mancha / Oxidação", "PAD Baço", "PAD Buraco",
    "PAD Buraco / Pico", "PAD Vibrado", "PAD Retoque", "COMMENTAIRE"
]

DEFEITOS_PNC      = [c for c in COLUNAS_MAYA if c.startswith("PNC ")]
DEFEITOS_PAD      = [c for c in COLUNAS_MAYA if c.startswith("PAD ")]
TODOS_DEFEITOS    = DEFEITOS_PNC + DEFEITOS_PAD
COLUNAS_NUMERICAS = ["QTE", "BONNES", "PNC", "PAD", "BPC"] + TODOS_DEFEITOS

# =============================================================================
# ESTILOS UTILITÁRIOS
# =============================================================================
def _thin(cor="CCCCCC"):
    s = Side(style="thin", color=cor)
    return Border(left=s, right=s, top=s, bottom=s)

def estilo_cabecalho(ws, row, col, valor, cor_fill="1F4E79", cor_fonte="FFFFFF"):
    cell = ws.cell(row=row, column=col, value=valor)
    cell.fill      = PatternFill("solid", fgColor=cor_fill)
    cell.font      = Font(bold=True, color=cor_fonte, size=9)
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border    = _thin("FFFFFF")

def estilo_valor(ws, row, col, valor, cor_fill="FFFFFF", bold=False):
    cell = ws.cell(row=row, column=col, value=valor)
    cell.fill      = PatternFill("solid", fgColor=cor_fill)
    cell.font      = Font(bold=bold, size=9)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border    = _thin("CCCCCC")
    return cell

def _pct_segura(numerador, denominador):
    """Devolve float de percentagem ou 0, sem exceções."""
    num = numerador if pd.notna(numerador) else 0
    den = denominador if pd.notna(denominador) else 0
    return float(num) / float(den) if den > 0 else 0.0

def construir_graficos_especificos_up(wb, df_pivot_up, nome_sheet, titulo_up):
    ws_g = wb.create_sheet(nome_sheet)
    ws_g.sheet_view.showGridLines = False

    cab = ws_g.cell(row=1, column=1,
                    value=f"RANKING DE DEFEITOS — SETOR: {titulo_up.upper()}")
    cab.font  = Font(bold=True, size=14, color="FFFFFF")
    cab.fill  = PatternFill("solid", fgColor="1F4E79")
    ws_g.merge_cells(start_row=1, start_column=1, end_row=1, end_column=10)
    ws_g.row_dimensions[1].height = 30

    construir_caixa_resumo(ws_g, df_pivot_up,
                           linha_inicio=3,
                           coluna_inicio=5)

    construir_tabela_top_defeitos(ws_g, df_pivot_up,
                                   linha_inicio=3,
                                   coluna_inicio=1)
    return 0    

# =============================================================================
# SHEET 3 — TABELA AGREGADA POR UP + ARTICLE
# =============================================================================
def construir_sheet3_por_up(ws, df_sheet1):
    for col in COLUNAS_NUMERICAS:
        if col in df_sheet1.columns:
            df_sheet1[col] = pd.to_numeric(df_sheet1[col], errors="coerce").fillna(0)

    agg      = {c: "sum" for c in COLUNAS_NUMERICAS if c in df_sheet1.columns}
    df_pivot = df_sheet1.groupby(["UP", "ARTICLE"], as_index=False).agg(agg)

    ordem_up        = {up: i for i, up in enumerate(UPS_FIXOS)}
    df_pivot["_ord"] = df_pivot["UP"].map(ordem_up).fillna(99)
    df_pivot         = df_pivot.sort_values(["_ord", "ARTICLE"]).drop(columns="_ord")
    df_pivot         = df_pivot.reset_index(drop=True)

    cabecalhos = ["UP", "ARTICLE", "Soma de QTE", "Soma de BONNES",
                  "Soma de PNC", "Soma de PAD", "%BPC", "%PNC", "%PAD"]
    cabecalhos += [f"Soma de {d}" for d in TODOS_DEFEITOS]
    n_cols     = len(cabecalhos)
    ultima_col = get_column_letter(n_cols)

    # ── Índices das colunas-chave (1-based) ───────────────────────────────────
    idx = {cab: i + 1 for i, cab in enumerate(cabecalhos)}
    col_qte    = get_column_letter(idx["Soma de QTE"])
    col_bonnes = get_column_letter(idx["Soma de BONNES"])
    col_pnc    = get_column_letter(idx["Soma de PNC"])
    col_pad    = get_column_letter(idx["Soma de PAD"])

    # ── Larguras de coluna ────────────────────────────────────────────────────
    ws.column_dimensions["A"].width = 20  # UP
    ws.column_dimensions["B"].width = 24  # ARTICLE
    for ci in range(3, n_cols + 1):
        ws.column_dimensions[get_column_letter(ci)].width = 9

    # ── Linha 1 — Cabeçalhos com texto vertical ───────────────────────────────
    ws.row_dimensions[1].height = 90

    cores_cab = {
        "UP":             ("1F4E79", "FFFFFF"),
        "ARTICLE":        ("1F4E79", "FFFFFF"),
        "Soma de QTE":    ("70AD47", "FFFFFF"),
        "Soma de BONNES": ("70AD47", "FFFFFF"),
        "Soma de PNC":    ("FFC000", "000000"),
        "Soma de PAD":    ("FF0000", "FFFFFF"),
        "%BPC":           ("D9E1F2", "000000"),
        "%PNC":           ("FFC000", "000000"),
        "%PAD":           ("FF0000", "FFFFFF"),
    }

    for ci, cab in enumerate(cabecalhos, start=1):
        if cab.startswith("Soma de PNC"):
            cor_f, cor_t = ("FFC000", "000000")
        elif cab.startswith("Soma de PAD"):
            cor_f, cor_t = ("FF0000", "FFFFFF")
        else:
            cor_f, cor_t = cores_cab.get(cab, ("DDDDDD", "000000"))

        cell            = ws.cell(row=1, column=ci, value=cab)
        cell.fill       = PatternFill("solid", fgColor=cor_f)
        cell.font       = Font(bold=True, color=cor_t, size=9)
        cell.alignment  = Alignment(horizontal="center", vertical="center",
                                    wrap_text=True, text_rotation=90)
        cell.border     = _thin("FFFFFF")

    # ── Ordenação dos UPs ─────────────────────────────────────────────────────
    ups_no_pivot  = df_pivot["UP"].unique()
    ups_ordenados = [u for u in UPS_FIXOS if u in ups_no_pivot]
    ups_ordenados += [u for u in ups_no_pivot if u not in ups_ordenados]

    excel_row            = 2
    ultima_linha_artigos = 2
    linhas_subtotal_up   = {}   # up_nome → linha excel do subtotal

    for up_nome in ups_ordenados:
        df_up    = df_pivot[df_pivot["UP"] == up_nome]
        artigos  = df_up.reset_index(drop=True)
        n_art    = len(artigos)

        # ── Linha separadora entre grupos (fundo cinzento claro) ──────────────
        if excel_row > 2:
            for ci in range(1, n_cols + 1):
                cell_sep        = ws.cell(row=excel_row, column=ci, value="")
                cell_sep.fill   = PatternFill("solid", fgColor="F2F2F2")
                cell_sep.border = _thin("E0E0E0")
            ws.row_dimensions[excel_row].height = 6
            excel_row += 1

        # ── Linha de subtotal do UP ───────────────────────────────────────────
        linha_sub              = excel_row
        linhas_subtotal_up[up_nome] = linha_sub
        linha_art_ini          = excel_row + 1
        linha_art_fim          = excel_row + n_art

        # Col A — nome do UP (verde claro, negrito)
        cell_a            = ws.cell(row=linha_sub, column=1, value=up_nome)
        cell_a.fill       = PatternFill("solid", fgColor="E2EFDA")
        cell_a.font       = Font(bold=True, size=9)
        cell_a.alignment  = Alignment(horizontal="left", vertical="center")
        cell_a.border     = _thin("CCCCCC")

        # Col B — vazia, mesmo fundo
        cell_b            = ws.cell(row=linha_sub, column=2, value="")
        cell_b.fill       = PatternFill("solid", fgColor="E2EFDA")
        cell_b.font       = Font(bold=True, size=9)
        cell_b.alignment  = Alignment(horizontal="center", vertical="center")
        cell_b.border     = _thin("CCCCCC")

        # Colunas de dados — fórmulas SUM sobre os artigos do grupo
        for ci, cab in enumerate(cabecalhos[2:], start=3):
            campo    = cab.replace("Soma de ", "")
            cl       = get_column_letter(ci)

            if campo == "%BPC":
                v = (f"=IF(SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim})>0,"
                     f"SUM({col_bonnes}{linha_art_ini}:{col_bonnes}{linha_art_fim})/"
                     f"SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim}),0)")
            elif campo == "%PNC":
                v = (f"=IF(SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim})>0,"
                     f"SUM({col_pnc}{linha_art_ini}:{col_pnc}{linha_art_fim})/"
                     f"SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim}),0)")
            elif campo == "%PAD":
                v = (f"=IF(SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim})>0,"
                     f"SUM({col_pad}{linha_art_ini}:{col_pad}{linha_art_fim})/"
                     f"SUM({col_qte}{linha_art_ini}:{col_qte}{linha_art_fim}),0)")
            else:
                v = f"=SUM({cl}{linha_art_ini}:{cl}{linha_art_fim})"

            cell            = ws.cell(row=linha_sub, column=ci, value=v)
            cell.fill       = PatternFill("solid", fgColor="E2EFDA")
            cell.font       = Font(bold=True, size=9)
            cell.alignment  = Alignment(horizontal="center", vertical="center")
            cell.border     = _thin("CCCCCC")
            if "%" in campo:
                cell.number_format = "0.0%"

        excel_row += 1  # primeira linha de artigo

        # ── Linhas dos artigos ────────────────────────────────────────────────
        for _, row in artigos.iterrows():
            # Col A — UP em texto invisível (cinzento claro) para que o filtro funcione
            cell_a            = ws.cell(row=excel_row, column=1, value=up_nome)
            cell_a.fill       = PatternFill("solid", fgColor="FFFFFF")
            cell_a.font       = Font(size=9, color="D9D9D9")
            cell_a.alignment  = Alignment(horizontal="left", vertical="center")
            cell_a.border     = _thin("CCCCCC")

            # Col B — ARTICLE
            cell_b            = ws.cell(row=excel_row, column=2, value=row["ARTICLE"])
            cell_b.fill       = PatternFill("solid", fgColor="FFFFFF")
            cell_b.font       = Font(size=9)
            cell_b.alignment  = Alignment(horizontal="left", vertical="center")
            cell_b.border     = _thin("CCCCCC")

            for ci, cab in enumerate(cabecalhos[2:], start=3):
                campo = cab.replace("Soma de ", "")
                if campo == "%BPC":
                    v = _pct_segura(row.get("BONNES", 0), row.get("QTE", 0))
                elif campo == "%PNC":
                    v = _pct_segura(row.get("PNC", 0), row.get("QTE", 0))
                elif campo == "%PAD":
                    v = _pct_segura(row.get("PAD", 0), row.get("QTE", 0))
                else:
                    v = row.get(campo, 0)
                    v = float(v) if pd.notna(v) else 0.0

                cell = estilo_valor(ws, excel_row, ci, v, "FFFFFF")
                if "%" in campo:
                    cell.number_format = "0.0%"

            ultima_linha_artigos = excel_row
            excel_row += 1

    # ── Filtro e freeze ───────────────────────────────────────────────────────
    ws.auto_filter.ref = f"A1:{ultima_col}{ultima_linha_artigos}"
    ws.freeze_panes    = "C2"

    return ws

# =============================================================================
# CAIXA DE RESUMO %BPC / %PNC / %PAD  (usada em cada folha de UP)
# =============================================================================
def construir_caixa_resumo(ws, df_pivot_up, linha_inicio=3, coluna_inicio=1):
    total_qte = df_pivot_up["QTE"].sum() if "QTE" in df_pivot_up.columns else 0
    total_bonnes = df_pivot_up["BONNES"].sum() if "BONNES" in df_pivot_up.columns else 0
    total_pnc = df_pivot_up["PNC"].sum() if "PNC" in df_pivot_up.columns else 0
    total_pad = df_pivot_up["PAD"].sum() if "PAD" in df_pivot_up.columns else 0

    pct_bpc = _pct_segura(total_bonnes, total_qte)  # BONNES / QTE, igual à tabela dinâmica
    pct_pnc = _pct_segura(total_pnc, total_qte)
    pct_pad = _pct_segura(total_pad, total_qte)

    configs = [
        (0, "%BPC", "EDEDED", "000000", pct_bpc),
        (2, "%PNC", "FFC000", "000000", pct_pnc),
        (4, "%PAD", "C00000", "FFFFFF", pct_pad),
    ]

    borda = Side(style="medium", color="AAAAAA")

    for offset_col, label, cor_fill, cor_font, valor in configs:
        col_real = coluna_inicio + offset_col
        ws.column_dimensions[get_column_letter(col_real)].width = 12
        if offset_col < 4:
            ws.column_dimensions[get_column_letter(col_real + 1)].width = 2

        c_cab            = ws.cell(row=linha_inicio, column=col_real, value=label)
        c_cab.fill       = PatternFill("solid", fgColor=cor_fill)
        c_cab.font       = Font(bold=True, size=10, color=cor_font)
        c_cab.alignment  = Alignment(horizontal="center", vertical="center")
        c_cab.border     = Border(left=borda, right=borda, top=borda,
                                  bottom=Side(style="thin", color="CCCCCC"))
        ws.row_dimensions[linha_inicio].height = 22

        c_val               = ws.cell(row=linha_inicio + 1, column=col_real, value=valor)
        c_val.number_format = "0.0%"
        c_val.fill          = PatternFill("solid", fgColor=cor_fill)
        c_val.font          = Font(bold=True, size=13, color=cor_font)
        c_val.alignment     = Alignment(horizontal="center", vertical="center")
        c_val.border        = Border(left=borda, right=borda, bottom=borda,
                                     top=Side(style="thin", color="CCCCCC"))
        ws.row_dimensions[linha_inicio + 1].height = 26

    return linha_inicio + 3

# =============================================================================
# TABELA RESUMO — TOP 3 ARTIGOS POR DEFEITO (espelha os gráficos)
# =============================================================================
def construir_tabela_top_defeitos(ws, df_pivot_up, linha_inicio=3, coluna_inicio=8):
    """
    Para cada tipo de defeito com ocorrências, apresenta os Top 3 artigos
    com maior quantidade — estrutura idêntica à dos gráficos.
    Colunas: [Nome do Defeito] [Artigo] [Qtd]
    """
    borda_thin  = Side(style="thin",   color="CCCCCC")
    borda_med   = Side(style="medium", color="AAAAAA")
    b_dados     = Border(left=borda_thin, right=borda_thin,
                         top=borda_thin,  bottom=borda_thin)
    b_titulo    = Border(left=borda_med,  right=borda_med,
                         top=borda_med,   bottom=borda_med)

    COR_PNC_CAB  = "FFC000"   # laranja — cabeçalho de defeito PNC
    COR_PNC_LIN  = "FFF2CC"   # amarelo claro — linhas PNC
    COR_PAD_CAB  = "C00000"   # vermelho escuro — cabeçalho de defeito PAD
    COR_PAD_LIN  = "FFE7E7"   # vermelho claro — linhas PAD
    
    # ── Larguras fixas das 3 colunas da tabela ────────────────────────────────
    ws.column_dimensions[get_column_letter(coluna_inicio)].width     = 26  # Defeito
    ws.column_dimensions[get_column_letter(coluna_inicio + 1)].width = 26  # Artigo
    ws.column_dimensions[get_column_letter(coluna_inicio + 2)].width = 8   # Qtd

    linha_atual = linha_inicio

    # ── Título geral da tabela ────────────────────────────────────────────────
    ws.row_dimensions[linha_atual].height = 22
    t = ws.cell(row=linha_atual, column=coluna_inicio,
                value="📋 TOP 3 ARTIGOS POR DEFEITO")
    t.fill      = PatternFill("solid", fgColor="1F4E79")
    t.font      = Font(bold=True, size=9, color="FFFFFF")
    t.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    t.border    = b_titulo
    ws.merge_cells(start_row=linha_atual, start_column=coluna_inicio,
                   end_row=linha_atual,   end_column=coluna_inicio + 2)
    linha_atual += 1

    # ── Cabeçalho de colunas ──────────────────────────────────────────────────
    ws.row_dimensions[linha_atual].height = 16
    for i, texto in enumerate(["Defeito", "Artigo", "Qtd"]):
        c             = ws.cell(row=linha_atual, column=coluna_inicio + i, value=texto)
        c.fill        = PatternFill("solid", fgColor="2E75B6")
        c.font        = Font(bold=True, size=8, color="FFFFFF")
        c.alignment   = Alignment(horizontal="center", vertical="center")
        c.border      = b_dados
    linha_atual += 1

    # ── Blocos por defeito ────────────────────────────────────────────────────
    for defeito in TODOS_DEFEITOS:
        if defeito not in df_pivot_up.columns:
            continue

        # Reutiliza exatamente a mesma lógica dos gráficos
        top3 = (df_pivot_up[["ARTICLE", defeito]]
                .sort_values(by=defeito, ascending=False)
                .head(3))
        top3 = top3[top3[defeito] > 0]
        if top3.empty:
            continue

        eh_pnc   = defeito.startswith("PNC")
        cor_cab  = COR_PNC_CAB  if eh_pnc else COR_PAD_CAB
        cor_lin  = COR_PNC_LIN  if eh_pnc else COR_PAD_LIN
        cor_txt  = "000000"     if eh_pnc else "FFFFFF"
        prefixo  = "⚠ "         if eh_pnc else "🔴 "
        nome_cur = defeito.replace("PNC ", prefixo).replace("PAD ", prefixo)
        n_art    = len(top3)

        # Célula do nome do defeito — ocupa as linhas dos artigos (merge vertical)
        ws.merge_cells(start_row=linha_atual, start_column=coluna_inicio,
                       end_row=linha_atual + n_art - 1, end_column=coluna_inicio)
        c_def            = ws.cell(row=linha_atual, column=coluna_inicio, value=nome_cur)
        c_def.fill       = PatternFill("solid", fgColor=cor_cab)
        c_def.font       = Font(bold=True, size=8, color=cor_txt)
        c_def.alignment  = Alignment(horizontal="left", vertical="center",
                                     wrap_text=True, indent=1)
        c_def.border     = b_titulo

        # Linhas dos Top 3 artigos
        for pos, (_, fila) in enumerate(top3.iterrows()):
            ws.row_dimensions[linha_atual + pos].height = 15

            # Artigo
            c_art            = ws.cell(row=linha_atual + pos,
                                       column=coluna_inicio + 1,
                                       value=str(fila["ARTICLE"]))
            c_art.fill       = PatternFill("solid", fgColor=cor_lin)
            c_art.font       = Font(size=8)
            c_art.alignment  = Alignment(horizontal="left", vertical="center", indent=1)
            c_art.border     = b_dados

            # Quantidade
            c_qtd            = ws.cell(row=linha_atual + pos,
                                       column=coluna_inicio + 2,
                                       value=int(fila[defeito]))
            c_qtd.fill = PatternFill("solid", fgColor="FFFFFF")   # ← CORRETO
            c_qtd.font       = Font(bold=True, size=8)
            c_qtd.alignment  = Alignment(horizontal="center", vertical="center")
            c_qtd.border     = b_dados

        linha_atual += n_art

        # Linha separadora entre defeitos
        ws.row_dimensions[linha_atual].height = 4
        for ci in range(coluna_inicio, coluna_inicio + 3):
            sep        = ws.cell(row=linha_atual, column=ci, value="")
            sep.fill   = PatternFill("solid", fgColor="D9D9D9")
            sep.border = Border()
        linha_atual += 1    

    return linha_atual    

# =============================================================================
# MENU DE NAVEGAÇÃO
# =============================================================================
def construir_menu(wb, ups_gerados):
    ws_menu = wb.create_sheet("Menu", 0)
    ws_menu.sheet_view.showGridLines = False
    ws_menu.column_dimensions["A"].width = 40
    ws_menu.column_dimensions["B"].width = 20

    titulo           = ws_menu.cell(row=1, column=1,
                                    value="PAINEL DE CONTROLO — QUALIDADE")
    titulo.font      = Font(bold=True, size=16, color="FFFFFF")
    titulo.fill      = PatternFill("solid", fgColor="1F4E79")
    titulo.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws_menu.row_dimensions[1].height = 40
    ws_menu.cell(row=1, column=2).fill = PatternFill("solid", fgColor="1F4E79")

    ws_menu.row_dimensions[3].height = 25
    sec1           = ws_menu.cell(row=3, column=1,
                                  value="📋 TABELAS E DADOS AGREGADOS")
    sec1.font      = Font(bold=True, size=11, color="FFFFFF")
    sec1.fill      = PatternFill("solid", fgColor="2E75B6")
    sec1.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws_menu.cell(row=3, column=2).fill = PatternFill("solid", fgColor="2E75B6")

    cell_s3           = ws_menu.cell(row=4, column=1,
                                     value="→ Ver Tabela de Dados Completa (Sheet3)")
    cell_s3.hyperlink = "#Sheet3!A1"
    cell_s3.font      = Font(color="1F4E79", underline="single", size=10)
    cell_s3.alignment = Alignment(horizontal="left", vertical="center", indent=3)

    ws_menu.row_dimensions[6].height = 25
    sec2           = ws_menu.cell(row=6, column=1,
                                  value="📊 GRÁFICOS DE PERFORMANCE POR UP")
    sec2.font      = Font(bold=True, size=11, color="FFFFFF")
    sec2.fill      = PatternFill("solid", fgColor="C00000")
    sec2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws_menu.cell(row=6, column=2).fill = PatternFill("solid", fgColor="C00000")

    cores_menu = ["F2F2F2", "EBF3FB"]

    for i, up in enumerate(ups_gerados):
        linha     = 7 + i
        nome_graf = f"G_{str(up)[:28]}"
        cor       = cores_menu[i % len(cores_menu)]

        ws_menu.row_dimensions[linha].height = 22
        cell_up           = ws_menu.cell(row=linha, column=1,
                                         value=f"→ Aceder Gráficos: {up.upper()}")
        cell_up.hyperlink = f"#{nome_graf}!A1"
        cell_up.font      = Font(color="000000", underline="single", size=10)
        cell_up.fill      = PatternFill("solid", fgColor=cor)
        cell_up.alignment = Alignment(horizontal="left", vertical="center", indent=5)
        ws_menu.cell(row=linha, column=2).fill = PatternFill("solid", fgColor=cor)

    return ws_menu


# =============================================================================
# PROCESSAMENTO PRINCIPAL
# =============================================================================
def processar_ficheiro():
    if not os.path.exists(CAMINHO_REFERENCIAS):
        messagebox.showerror("Erro",
            f"Ficheiro de referências não encontrado:\n{CAMINHO_REFERENCIAS}")
        return

    df_refs         = pd.read_excel(CAMINHO_REFERENCIAS)
    df_refs.columns = df_refs.columns.str.strip()

    mapa_up = dict(zip(
        df_refs["ARTICLE"].astype(str).str.strip(),
        df_refs["UP"].astype(str).str.strip()
    ))

    file_path = filedialog.askopenfilename(
        title="Selecionar B2C4.xlsx", filetypes=[("Excel", "*.xlsx")])
    if not file_path:
        return

    try:
        df_origem         = pd.read_excel(file_path)
        df_origem.columns = (df_origem.columns.str.strip()
                             .str.replace("ILÔT", "UP")
                             .str.replace("ILOT", "UP"))
        n_linhas = len(df_origem)

        data = {}
        for col in COLUNAS_MAYA:
            if col == "UP":
                data["UP"] = (
                    df_origem["ARTICLE"].astype(str).str.strip()
                    .map(mapa_up).fillna("").values
                    if "ARTICLE" in df_origem.columns else [""] * n_linhas
                )
            elif col in df_origem.columns:
                data[col] = df_origem[col].values
            else:
                data[col] = [""] * n_linhas
        df_final = pd.DataFrame(data)

        timestamp     = datetime.now().strftime("%Y%m%d_%H%M")
        nome_ficheiro = f"DADOS_MAYA_{timestamp}.xlsx"
        pasta_destino = filedialog.askdirectory(title="Escolher pasta para guardar o ficheiro")
        if not pasta_destino:
            pasta_destino = os.path.join(os.path.expanduser("~"), "Desktop")
        output_path = os.path.join(pasta_destino, nome_ficheiro)

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df_final.to_excel(writer, sheet_name="Sheet1", index=False)
            df_refs.to_excel(writer,  sheet_name="Sheet2", index=False)

        wb  = load_workbook(output_path)
        ws3 = wb.create_sheet("Sheet3")
        construir_sheet3_por_up(ws3, df_final.copy())

        ups_nos_dados = set(df_final["UP"].dropna().unique()) - {""}
        ups_reais     = [u for u in UPS_FIXOS if u in ups_nos_dados]
        ups_reais    += [u for u in df_final["UP"].dropna().unique()
                         if u not in ups_reais and u != ""]

        total_graficos = 0

        for up_nome in ups_reais:
            df_up = df_final[df_final["UP"] == up_nome].copy()
            for col in COLUNAS_NUMERICAS:
                if col in df_up.columns:
                    df_up[col] = pd.to_numeric(df_up[col], errors="coerce").fillna(0)

            agg_up      = {c: "sum" for c in COLUNAS_NUMERICAS if c in df_up.columns}
            df_pivot_up = df_up.groupby("ARTICLE", as_index=False).agg(agg_up)

            nome_aba        = f"G_{str(up_nome)[:28]}"
            qtd             = construir_graficos_especificos_up(wb, df_pivot_up,
                                                                 nome_aba, up_nome)
            total_graficos += qtd

        construir_menu(wb, ups_reais)
        wb.save(output_path)

        preenchidos = (df_final["UP"] != "").sum()
        messagebox.showinfo("Sucesso",
            f"✅ {n_linhas} linhas processadas!\n"
            f"🔗 {preenchidos} linhas com UP preenchido.\n"
            f"Guardado em: {pasta_destino}")
        os.startfile(output_path)

    except Exception as e:
        import traceback
        messagebox.showerror("Erro Crítico",
            f"Erro no processamento:\n{str(e)}\n\n{traceback.format_exc()}")


# =============================================================================
# INTERFACE
# =============================================================================
root = tk.Tk()
root.title("Gerador - Evolução BPC Interno")
root.geometry("300x150")

tk.Button(root, text="IMPORTAR FICHEIRO\nE GERAR TABELA",
          command=processar_ficheiro, bg="#0078D7", fg="white",
          font=("Arial", 10, "bold"), padx=20, pady=20).pack(expand=True)

root.mainloop()
