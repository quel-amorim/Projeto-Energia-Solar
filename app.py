from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  resultado = None

  if request.method == "POST":
    consumo_kwh = float(request.form.get("consumo", 0))
    tipo_ligacao = request.form.get("ligacao", "monofasico")

    # Dados de financiamento vindos do formulário
    prazo_meses = int(
        request.form.get("prazo", 60)
    )  # Ex: 60 meses (5 anos) ou 120 (10 anos)
    taxa_juros_anual = float(
        request.form.get("juros", 15.0)
    )  # Ex: 15% ao ano (~1.17% ao mês)

    # Regras CEEE Equatorial
    tarifa_kwh = 0.92
    min_kwh = {"monofasico": 30, "bifasico": 50, "trifasico": 100}
    consumo_minimo = min_kwh.get(tipo_ligacao, 30)

    consumo_faturado = max(consumo_kwh, consumo_minimo)
    custo_atual_mensal = consumo_faturado * tarifa_kwh

    #Viabilidade Solar
    geracao_por_kwp = 120
    potencia_necessaria_kwp = consumo_kwh / geracao_por_kwp
    custo_por_kwp = 4200.0
    custo_total_instalacao = potencia_necessaria_kwp * custo_por_kwp

    custo_novo_mensal = consumo_minimo * tarifa_kwh
    economia_mensal = custo_atual_mensal - custo_novo_mensal
    economia_anual = economia_mensal * 12

    #Simulação de Financiamento
    taxa_juros_mes = (taxa_juros_anual / 100) / 12

    if taxa_juros_mes > 0:
      prestacao_mensal = (
          custo_total_instalacao
          * (taxa_juros_mes * (1 + taxa_juros_mes) ** prazo_meses)
          / ((1 + taxa_juros_mes) ** prazo_meses - 1)
      )
    else:
      prestacao_mensal = custo_total_instalacao / prazo_meses

    saldo_mensal_durante_financiamento = economia_mensal - prestacao_mensal

    resultado = {
        "consumo_faturado": consumo_faturado,
        "custo_atual_mensal": round(custo_atual_mensal, 2),
        "potencia_necessaria": round(potencia_necessaria_kwp, 2),
        "custo_instalacao": round(custo_total_instalacao, 2),
        "economia_mensal": round(economia_mensal, 2),
        "prestacao_mensal": round(prestacao_mensal, 2),
        "saldo_mensal": round(saldo_mensal_durante_financiamento, 2),
        "prazo_meses": prazo_meses,
    }

  return render_template("pagVisual.html", resultado=resultado)


if __name__ == "__main__":
  app.run(debug=True)