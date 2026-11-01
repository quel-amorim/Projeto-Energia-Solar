# ☀️ Simulador Solar & Financiamento (CEEE Equatorial)

Um sistema web desenvolvido em **Python** com **Flask** para calcular a viabilidade financeira e técnica da instalação de painéis solares residenciais/comerciais atendidos pela concessionária **CEEE Equatorial** (Rio Grande do Sul), incluindo uma simulação completa de financiamento bancário via Tabela Price.

## 🎯 Objetivo do Projeto

O objetivo desta aplicação é ajudar o consumidor a entender:

1. Quanto ele paga atualmente em sua conta de luz considerando a tarifa da CEEE Equatorial e a taxa mínima de disponibilidade da rede.

2. O dimensionamento recomendado do sistema fotovoltaico (em kWp) e o valor aproximado do investimento.

3. A economia mensal e anual gerada pela energia solar.

4. O impacto no bolso ao financiar o projeto, comparando a economia na conta de luz com a parcela do financiamento.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.x, Flask

* **Frontend:** HTML5, CSS3 (Design Responsivo)

* **Algoritmos Financeiros:** Tabela Price (PMT) e Regras Tarifárias Nacionais/Locais

## 📊 Regras e Lógica de Cálculo

### 1. CEEE Equatorial (Tarifa e Taxa Mínima)

A CEEE Equatorial cobra uma taxa mínima de disponibilidade de acordo com o padrão de entrada da residência:

* **Monofásico:** 30 kWh

* **Bifásico:** 50 kWh

* **Trifásico:** 100 kWh

O valor faturado da conta é o maior valor entre o consumo real do usuário e a taxa mínima da sua ligação, multiplicado pela tarifa estimada da concessionária (com impostos inclusos).

### 2. Dimensionamento Fotovoltaico

* Considera-se a irradiação solar média do Estado do Rio Grande do Sul, onde **1 kWp** instalado produz em média **120 kWh/mês**.

* **Potência Recomendada (kWp)** = $\frac{\text{Consumo Mensal (kWh)}}{120}$

* **Custo Estimado da Instalação** = $\text{Potência (kWp)} \times \text{R\$ 4.200,00}$ *(Valor médio de mercado incluindo painéis, inversor, estrutura e mão de obra/homologação)*.

### 3. Simulação de Financiamento (Tabela Price)

A prestação mensal ($PMT$) do empréstimo bancário é calculada através da fórmula:

$$
PMT = PV \times \frac{i(1+i)^n}{(1+i)^n - 1}
$$

Onde:

* $PV$ = Valor do investimento (Custo total do sistema)

* $i$ = Taxa de juros mensal

* $n$ = Prazo do financiamento em meses

O sistema compara a **Economia Mensal na Conta** com a **Parcela do Banco** para identificar se o cliente tem fluxo de caixa positivo imediato.

## 📁 Estrutura do Projeto

```
projeto_solar_ceee/
│
├── app.py             # Aplicação principal Flask e lógica dos cálculos
├── README.md          # Documentação do projeto
├── templates/
│   └── pagVisual.html     # Formulário de entrada e exibição dos resultados
└── static/
    └── estilos.css      # Estilização visual da interface

```

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

* **Python 3.8+** instalado na sua máquina.

### Passo a Passo

1. **Clone ou baixe o repositório:**

   ```
   git clone https://github.com/seu-usuario/simulador-solar-ceee.git
   cd simulador-solar-ceee
   
   ```

2. **Crie e ative um ambiente virtual (Opcional, mas recomendado):**

   * no Windows:

     ```
     python -m venv venv
     venv\Scripts\activate
     
     ```

   * no Linux/Mac:

     ```
     python3 -m venv venv
     source venv/bin/activate
     
     ```

3. **Instale as dependências:**

   ```
   pip install flask
   
   ```

4. **Execute a aplicação:**

   ```
   python app.py
   
   ```

5. **Acesse no seu navegador:**
   Abra o endereço `http://127.0.0.1:5000` para utilizar o simulador.


## 📜 Licença

Este projeto é um protótipo educacional desenvolvido para fins de estudos e demonstração técnica. Sinta-se livre para adaptar e utilizar!
