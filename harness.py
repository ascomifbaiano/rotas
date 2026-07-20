import os
import json
import time
import sys
from datetime import datetime

class RotaFrotaHarness:
    """
    Test Harness Library para validação automatizada e diagnóstico de integridade
    da aplicação Roteirizador de Frota do IF Baiano.
    """
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.base_dir, 'index.html')
        self.json_path = os.path.join(self.base_dir, 'postos.json')
        self.report_path = os.path.join(self.base_dir, 'harness_report.md')
        
    def run_suite(self):
        print("=" * 65)
        print("   IF BAIANO FLEET SYSTEMS - DIAGNOSTIC HARNESS")
        print("=" * 65)
        print(f"[INFO] Sensores ativos na base: {self.base_dir}")
        
        start_time = time.perf_counter()
        tests = []
        
        # Teste 1: Existência dos arquivos essenciais
        print("\n[Varredura] Checando arquivos estáticos de imagem...")
        images = [
            'marca-if-baiano-horizontal-branca.png',
            'marca-if-baiano-horizontal.png'
        ]
        img_missing = []
        for img in images:
            img_path = os.path.join(self.base_dir, img)
            if not os.path.exists(img_path):
                img_missing.append(img)
                
        if not img_missing:
            tests.append({"nome": "Imagens de Marca Institucional", "status": "OK", "detalhe": "Logotipos horizontal normal e contraste encontrados."})
            print("  [OK] Imagens institucionais validadas.")
        else:
            tests.append({"nome": "Imagens de Marca Institucional", "status": "FALHA", "detalhe": f"Faltando logotipos: {', '.join(img_missing)}"})
            print(f"  [FALHA] Imagens ausentes: {img_missing}")

        # Teste 2: Integridade estrutural do index.html
        print("[Varredura] Analisando index.html...")
        if not os.path.exists(self.html_path):
            tests.append({"nome": "Integridade do index.html", "status": "FALHA", "detalhe": "Arquivo index.html nao encontrado na raiz."})
            print("  [FALHA] Arquivo index.html ausente.")
        else:
            try:
                with open(self.html_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Elementos críticos exigidos para funcionamento
                critical_elements = {
                    "Leaflet CSS": "leaflet.css",
                    "Leaflet JS": "leaflet.js",
                    "Outfit Font": "family=Outfit",
                    "Inter Font": "family=Inter",
                    "Origem Select ID": 'id="origem"',
                    "Destino Select ID": 'id="destino"',
                    "Veiculo Select ID": 'id="veiculo"',
                    "Nivel Combustivel ID": 'id="nivel-combustivel"',
                    "Map Container ID": 'id="map"',
                    "Autonomia Gauge ID": 'id="gauge-fill"',
                    "Distance Element ID": 'id="stat-dist"',
                    "Time Element ID": 'id="stat-time"',
                    "Fuel Element ID": 'id="stat-fuel"',
                    "Stops Element ID": 'id="stat-stops"',
                    "Custom A11y Toolbar": 'class="a11y-toolbar"'
                }
                
                missing_el = []
                for name, tag in critical_elements.items():
                    if tag not in content:
                        missing_el.append(name)
                        
                if not missing_el:
                    tests.append({"nome": "Integridade do index.html", "status": "OK", "detalhe": "Todos os containers, fontes e scripts essenciais estao presentes."})
                    print("  [OK] index.html validado com 100% dos elementos criticos.")
                else:
                    tests.append({"nome": "Integridade do index.html", "status": "FALHA", "detalhe": f"Elementos ausentes no HTML: {', '.join(missing_el)}"})
                    print(f"  [FALHA] Elementos ausentes no index.html: {missing_el}")
            except Exception as e:
                tests.append({"nome": "Integridade do index.html", "status": "FALHA", "detalhe": f"Erro de leitura: {str(e)}"})
                print(f"  [FALHA] Erro ao ler index.html: {e}")

        # Teste 3: Parse e validade de postos.json
        print("[Varredura] Validando postos.json...")
        if not os.path.exists(self.json_path):
            tests.append({"nome": "Parse de postos.json", "status": "FALHA", "detalhe": "Arquivo postos.json nao encontrado."})
            print("  [FALHA] Arquivo postos.json ausente.")
        else:
            try:
                with open(self.json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Valida chaves primarias
                campi = data.get("campi", [])
                postos = data.get("postos", [])
                
                if not campi or not postos:
                    tests.append({"nome": "Parse de postos.json", "status": "FALHA", "detalhe": "Estrutura JSON vazia ou sem chaves 'campi' e 'postos'."})
                    print("  [FALHA] Chaves primarias ausentes ou sem registros.")
                else:
                    # Valida chaves internas de um registro de exemplo
                    c_valid = "lat" in campi[0] and "lng" in campi[0] and "nome" in campi[0]
                    p_valid = "lat" in postos[0] and "lng" in postos[0] and "nome" in postos[0]
                    
                    if c_valid and p_valid:
                        tests.append({"nome": "Parse de postos.json", "status": "OK", "detalhe": f"JSON valido com {len(campi)} campi e {len(postos)} postos cadastrados."})
                        print(f"  [OK] postos.json validado. {len(campi)} campi, {len(postos)} postos.")
                    else:
                        tests.append({"nome": "Parse de postos.json", "status": "FALHA", "detalhe": "Campos obrigatorios (nome, lat, lng) ausentes em algum registro."})
                        print("  [FALHA] Formato de registro invalido em postos.json.")
            except Exception as e:
                tests.append({"nome": "Parse de postos.json", "status": "FALHA", "detalhe": f"Erro de sintaxe JSON: {str(e)}"})
                print(f"  [FALHA] Erro ao processar postos.json: {e}")
                
        elapsed = (time.perf_counter() - start_time) * 1000
        
        # Consolida relatorio
        self._write_report(tests, elapsed)
        
        success = all(t["status"] == "OK" for t in tests)
        print("\n" + "=" * 65)
        print(f"   DIAGNOSTICO CONCLUIDO: {'SUCESSO' if success else 'FALHA'}")
        print(f"   Tempo total: {elapsed:.2f} ms")
        print("=" * 65)
        
        return success

    def _write_report(self, tests, elapsed):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S") if 'datetime' in sys.modules else time.strftime("%d/%m/%Y %H:%M:%S")
        
        md = []
        md.append("# 🧪 Relatório de Diagnóstico & Integridade - Rota Frota IF Baiano\n")
        md.append(f"- **Data da Varredura**: `{now}`")
        md.append(f"- **Tempo de Processamento**: `{elapsed:.2f} ms``\n")
        
        md.append("## 📊 Tabela de Status dos Sensores\n")
        md.append("| Sensor / Teste | Status | Detalhes Técnicos |")
        md.append("|---|---|---|")
        
        for t in tests:
            icon = "🟢 OK" if t["status"] == "OK" else "🔴 FALHA"
            md.append(f"| {t['nome']} | {icon} | {t['detalhe']} |")
            
        md.append("\n---\n")
        md.append("*Diagnóstico de dobra espacial realizado pelos sensores do laboratório YLuna85 LABs.*")
        
        with open(self.report_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md))

if __name__ == "__main__":
    harness = RotaFrotaHarness()
    harness.run_suite()
