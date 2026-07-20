# 🚗 Roteirizador de Frota — IF Baiano

![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JS-ES6+-F7DF1E?logo=javascript&logoColor=black)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?logo=leaflet&logoColor=white)
![OSRM](https://img.shields.io/badge/OSRM-Routing-blue)

Aplicação web responsiva de planejamento logístico de viagens para a frota do **Instituto Federal Baiano**. Calcula rotas reais por rodovias, estima consumo de combustível e indica paradas obrigatórias em postos credenciados da rede **Goldi Fleet**, respeitando a reserva de segurança de 1/4 do tanque.

---

## 📖 1. Sobre

O roteirizador auxilia motoristas do IF Baiano a planejar trajetos intermunicipais entre os campi da instituição na Bahia. Funciona em qualquer dispositivo (PC, tablet ou celular) e não depende de APIs pagas.

### Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| **Rota real por rodovia** | Traçado via OSRM (Open Source Routing Machine), distância e tempo reais |
| **Reserva de 1/4** | O abastecimento é forçado antes de o tanque atingir 25% |
| **Nível inicial** | O motorista informa se o tanque está cheio, 3/4, metade ou 1/4 |
| **Gauge de combustível** | Barra visual que indica a proporção autonomia/distância |
| **Paradas numeradas** | Pins vermelhos no mapa na ordem cronológica de abastecimento |
| **Postos alternativos** | Pins verdes mostram opções adicionais da Goldi Fleet na rota |
| **Navegação GPS** | Links diretos para Google Maps e Waze no celular |
| **Mobile bottom sheet** | Painel deslizante com tabs no celular, mapa em tela cheia |
| **Acessibilidade** | Alto contraste (WCAG), ajuste de fonte (A+/A−), ARIA roles, focus-visible |
| **SEO** | Meta tags, Open Graph, semântica HTML5 |

---

## 📂 2. Estrutura

```
rota-frota/
├── index.html      ← Interface, estilos e lógica (single-file)
├── postos.json     ← Base de dados: campi + postos Goldi Fleet
└── README.md       ← Documentação
```

---

## 🧠 3. Lógica de Abastecimento

1. **Autonomia útil** = `(litros no tanque − reserva de 25%) × consumo km/L`
2. O algoritmo percorre a rota em km e, quando a autonomia útil restante não cobre o trecho até o destino, seleciona o posto credenciado **mais distante** que ainda fique **antes** do veículo entrar na reserva de segurança.
3. Após cada parada, o tanque é considerado cheio (100%) e o ciclo se repete.
4. Se não houver postos suficientes para cobrir o trajeto, um alerta crítico é exibido.

---

## 📝 4. Changelog

### [2.4.0] — 20/07/2026

**Atualização das Unidades do IF Baiano:**
- **Remoção de Unidades Inválidas**: Expurgadas as unidades/campi que não pertencem ao IF Baiano (como Candeias, Feira de Santana e destinos de suporte do IFBA).
- **Correção e Padronização de Endereços**: Atualizados os nomes (ex: "Catu" sem acento) e coordenadas geográficas (lat/lng) de todas as 14 unidades existentes e da Reitoria para máxima precisão de rotas.
- **Novas Unidades do Processo de Expansão**: Cadastradas as novas unidades em implantação de **Santo Estêvão**, **Remanso**, **Ruy Barbosa** e **Ribeira do Pombal** com coordenadas aproximadas das sedes municipais correspondentes.
- **Sincronização de Banco de Dados**: Atualizados os arquivos `postos.json` e a base interna (`dadosLocaisDefault`) no `index.html`.
- **Ajuste de Seleção Padrão**: Modificado o carregador dinâmico do dropdown para usar 'Campus Senhor do Bonfim' como destino pré-selecionado de fallback.

### [2.3.0] — 19/07/2026

**Repaginação Visual Premium (Aesthetic Overhaul):**
- **Nova Identidade Visual HSL**: Otimização total da folha de estilos com HSL institucional calibrado (verde/vermelho IF Baiano) e sombras finas de alta definição para evitar clichês e ruído visual.
- **Bento Grid de Estatísticas**: Estilização bento-style dos cartões com efeitos táteis de escala e realce dinâmico por bordas indicadoras de status.
- **CartoDB Voyager Map Tiles**: Substituição da camada de mapa OSM convencional pela CartoDB Voyager, tornando o traçado das rotas e a identificação de postos/campi infinitamente mais limpos e contrastados.
- **Dial de Combustível Premium**: Visual repaginado para o medidor de combustível semicircular SVG com estilo esportivo/instrumental e agulha iluminada.

### [2.2.1] — 17/07/2026

**Expansão da Frota:**
- **Inclusão de Novos Veículos**: Adicionados os veículos **Hyundai HB20 1.0 Automático (Gasolina)**, **Fiat Toro Ranch Automática (Gasolina)** e **Fiat Toro Ranch Automática (Diesel)** à lista de opções da frota, com estimativas técnicas de consumo e capacidade de tanque prontas para suporte logístico e futuras atualizações de anos/modelos.

### [2.2.0] — 17/07/2026

**Branding e Identidade Institucional:**
- **Logotipos Oficiais Integrados**: Adicionados os logotipos institucionais reais em formato horizontal do **IF Baiano** no cabeçalho do portal, substituindo a representação SVG provisória.
- **Alternador de Alto Contraste Inteligente**: Configuradas as imagens de forma que a versão branca (`marca-if-baiano-horizontal-branca.png`) apareça em visualização convencional com fundo escuro, e a versão colorida convencional (`marca-if-baiano-horizontal.png`) seja ativada automaticamente no modo de alto contraste para conformidade e clareza visual de leitura.

### [2.1.0] — 17/07/2026

**Robustez e Dados Locais:**
- **Correção de CORS / Fallback Local**: Embutida a base de dados completa de campi, cidades e postos diretamente no arquivo `index.html`. Agora, se o usuário rodar a aplicação localmente (`file://`), a aplicação ativa um fallback transparente sem travar com selects vazios por bloqueio de CORS.
- **Expansão de Rotas e Destinos**: Adicionadas 9 grandes cidades da Bahia de relevância logística (Vitória da Conquista, Juazeiro, Barreiras, SAJ, Ilhéus/Itabuna, Lençóis, Paulo Afonso, Porto Seguro) e a Capital Federal (Brasília - DF).
- **Postos Rota Centro-Oeste**: Cadastrados postos credenciados da Goldi Fleet ao longo das rodovias BR-242 e BR-020 para permitir simulações realistas e seguras de longa distância (como Salvador a Brasília - DF, com 4 paradas estimadas no Gol 1.0).

### [2.0.0] — 17/07/2026

**UX e Responsividade:**
- Layout mobile-first: mapa ocupa tela cheia, sidebar se torna bottom sheet deslizante com alça de arrasto.
- Tabs mobile (Viagem / Resumo / Postos) para navegação rápida entre seções sem scroll.
- Grid de estatísticas em cards destacados (distância, tempo, combustível, paradas).
- Gauge visual de combustível com cores dinâmicas (verde → laranja → vermelho).
- Loading spinner no botão de cálculo com desativação durante requisição.
- Toast flutuante para erros em vez de `alert()` nativo.
- Empty states com ícones para seções sem dados.
- Legenda flutuante semitransparente sobre o mapa com glassmorphism.
- Animações de entrada suaves (slideUp) nos painéis de resultado.
- Breakpoints em 900px (tablet) e 400px (celular pequeno).

**Acessibilidade (WCAG):**
- Todos os botões com `aria-label` descritivo.
- ARIA roles (`banner`, `complementary`, `main`, `tablist`, `tab`, `alert`).
- `focus-visible` com outline verde em todos os elementos interativos.
- Alto contraste aplica `grayscale + contrast` nos tiles do mapa Leaflet.
- Links externos com `rel="noopener"`.

**Código:**
- JavaScript encapsulado em IIFE (sem poluição do escopo global).
- `DOMContentLoaded` em vez de `window.onload`.
- Mapa redimensiona automaticamente ao mudar viewport.
- `100dvh` como fallback para barras de navegação móveis.

### [1.5.0] — 19/07/2026
- 🗺️ **Botões de Rota GPS em Todos os Postos**: Cada posto listado no painel lateral (obrigatório ou alternativo) agora exibe três botões de navegação — 🗺️ Google Maps, 🧭 Waze e 🍎 Apple Maps — que abrem o aplicativo de rotas no celular ou no PC diretamente para aquele posto, com a origem já pré-configurada se estiver selecionada.
- 📍 **Clique Livre no Mapa**: Ao clicar em qualquer ponto do mapa (fora de um marcador de posto), um popup aparece com o nome do ponto selecionado, suas coordenadas e os mesmos três botões de navegação GPS para iniciar a rota até aquele ponto.
- 🔴 **Destaque Visual de Postos Obrigatórios**: Postos de parada obrigatória agora exibem borda esquerda vermelha e fundo levemente rosado para diferenciação visual imediata dos postos alternativos.
- 🍎 **Apple Maps Adicionado**: Adição do botão de Apple Maps em todos os pontos de navegação (marcadores de mapa e lista de postos), para compatibilidade com usuários de iPhone e Mac.

### [1.5.1] — 19/07/2026
- 🏫 **Favicon Oficial com Fundo Branco**: Geração do `favicon-if-baiano.ico` (multi-tamanho: 16–128px) e `favicon-if-baiano.png` com fundo branco, a partir da logo vertical oficial do Manual de Marca. Os arquivos mestres ficam em `3.4 Cores e Marcas do IF Baiano/` e são copiados para a raiz do projeto.
- 📋 **Diretriz no AGENTS.md**: Registrada no `AGENTS.md` a regra obrigatória de usar o favicon, a paleta de cores CSS e os logotipos oficiais do IF Baiano em todas as aplicações web institucionais criadas a partir de agora.


### [1.4.2] — 19/07/2026
- 🗺️ **Altura Rígida do Painel do Mapa**: Fixação da altura do `.map-panel` no desktop para `height: calc(100vh - 64px)` de forma a forçar a viewport do Leaflet a renderizar com altura total no flexbox (resolvendo o problema de mapas que encolhem até sumirem por falta de altura explícita em contêineres flex).

### [1.4.1] — 19/07/2026
- ⚡ **Resiliência na Inicialização**: Ajuste na inicialização Javascript via `document.readyState` para evitar que a aplicação fique inativa se o evento `DOMContentLoaded` já tiver sido disparado (comum em servidores locais rápidos ou iframes de preview).
- 📐 **Altura Rígida da Sidebar**: Fixação da altura da sidebar no desktop para `height: calc(100vh - 64px)` de forma a forçar a barra de rolagem vertical (scrollbar) e impedir o transbordo.

### [1.4.0] — 19/07/2026
- ⛽ **Medidor Invertido (Decrescente)**: Ajuste na orientação do dial de combustível para ser decrescente da esquerda para a direita (Cheio/100% no "C" da esquerda para Reserva/0% no "R" da direita).
- 📐 **Recolhimento Vertical (Accordion)**: Botões de toggle vertical (`▲` / `▼`) nos títulos dos cartões de seção (Viagem, Resumo e Postos) para recolher os painéis de informação e poupar espaço vertical na tela sem precisar rolar ou dar zoom out.
- 📜 **Barra de Rolagem Vertical (Scrollbar)**: Correção na restrição de altura da barra lateral (sidebar) para `height: 100%` e `max-height: 100%` com `box-sizing: border-box`, forçando a exibição correta e estilizada da barra de rolagem (scrollbar) quando o conteúdo excede a altura útil da janela.

### [1.3.0] — 19/07/2026
- ⛽ **Medidor de Combustível Interativo**: Mostrador analógico semicircular SVG com ponteiro dinâmico que gira ao clicar no arco ou na escala (incrementos de 10% de 0% a 100%).
- 🚫 **Bloqueio de Partida a 0%**: O cálculo da rota é bloqueado se o tanque estiver zerado, exigindo abastecimento inicial.
- 📐 **Sidebar Deslizante (Slide-out)**: Botão de toggle flutuante que recolhe o painel esquerdo para que o mapa ocupe 100% de largura no desktop, otimizando o zoom do trajeto.

### [1.2.0] — 19/07/2026
- 🎨 **Redesenho Impeccable (Estilo Premium IF Baiano)**: Remodelação visual completa da interface para remover padrões clichês (glassmorphism exagerado, faixas de borda "side-stripe" em cartões/listas e sombras pesadas).
- 🗺️ **Pins SVG Pulsantes**: Substituição dos marcadores padrão azuis do Leaflet por pins circulares SVG animados com efeito de pulso luminoso verde e vermelho.
- ⛽ **Dashboard de Autonomia**: Medidor de combustível com régua automotiva linear ("R", "1/2", "C") de apoio à autonomia útil.
- 🎨 **Paleta de Cores**: Unificação dos tokens de estilo baseados no Manual de Identidade Visual oficial do IF Baiano (verde e vermelho oficiais, fundo neutro harmonizado).

### [1.1.0] — 17/07/2026
- Lógica de nível inicial do tanque (100% a 25%).
- Reserva de segurança de 1/4 como regra inviolável.
- Algoritmo de mapeamento linear de postos por km da rota.
- Pins vermelhos numerados para paradas obrigatórias.

### [1.0.0] — 17/07/2026
- Lançamento: clone adaptado da BR-324 com identidade IF Baiano.
- Integração Leaflet + OSRM.
- Base de campi e postos Goldi Fleet.
- Links de navegação GPS (Google Maps + Waze).

---

*Desenvolvido sob as diretrizes de TI e Comunicação Social (DICOM) do Instituto Federal Baiano.*
