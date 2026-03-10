# **Redes e Sistemas Operativos**

### 1. UFCD 0773 - Instalação de Cabo UTP
- **Objetivo:** Crimpagem de cabo de rede Cat 6 com fichas RJ-45 (padrão T568B).
- **Competências:** Manuseamento de ferramentas (alicate, descarnador), teste de continuidade com cable tester.
- **Documentação:** [Relatório completo](./0773-rede-local-relatorio.docx)

**Labs práticos do curso Técnico de Informática – Sistemas**  
**Ferramentas:** Windows 10/11, comandos nativos, configuração manual

[![CV Técnico Redes](https://img.shields.io/badge/Relatório_Completo-PDF-blue?style=for-the-badge&logo=adobe-acrobat-reader)](link-do-teu-pdf)

---

## **Labs Práticos Realizados**

### **Lab 1 – Instalação Windows + Particionamento**
**O que fiz:** Instalação limpa Windows 10/11 em VM. Criei partições C: (sistema) e D: (dados) em NTFS.  
**Resultado:** Sistema operacional funcional com disco organizado.  
[Ver detalhes no relatório PDF](#)

### **Lab 2 – IP Estático + DNS Manual**
**O que fiz:** Configurei IP 192.168.1.10/24, gateway 192.168.1.1, DNS 8.8.8.8 numa máquina Windows.  
**Resultado:** Conectividade estável sem DHCP. Validado com `ipconfig /all`.  
[Ver configuração no relatório PDF](#)

### **Lab 3 – Diagnóstico de Conectividade**
**O que fiz:** Testes sistemáticos: `ipconfig`, `ping` (loopback/gateway/IP externo/DNS), `tracert`.  
**Resultado:** Metodologia para resolver 90% dos problemas de rede comuns.  
[Ver comandos e prints no relatório PDF](#)

---

## 📊 **Comandos**

```cmd
ipconfig /all     # Configuração completa da placa
ipconfig /release # Libera IP DHCP
ipconfig /renew   # Renova IP DHCP
ping 127.0.0.1    # Teste local TCP/IP
ping 192.168.1.1  # Teste gateway
ping 8.8.8.8      # Teste conectividade externa
ping google.com   # Teste resolução DNS
tracert google.com # Rastrear rota até destino

## Atividades de Redes


