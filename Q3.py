import json

# Exemplo de dados no formato JSON
faturamento_json = '''
{
  "SP": [200, 250, 180, 320, 220, 270],
  "RJ": [150, 200, 210, 270],
  "MG": [190, 220, 230, 210, 270],
  "ES": [100, 150, 200, 250, 190],
  "outros": [80, 100, 120]
}
'''

faturamento = json.loads(faturamento_json)

# Calculando o faturamento total e média
total_faturamento = sum(sum(valores) for valores in faturamento.values())
dias_com_faturamento = sum(len(valores) for valores in faturamento.values())
media_faturamento = total_faturamento / dias_com_faturamento

# Encontrando o menor e maior valor
menor_valor = min(min(valores) for valores in faturamento.values())
maior_valor = max(max(valores) for valores in faturamento.values())

# Contando os dias acima da média
dias_acima_media = sum(1 for valores in faturamento.values() for v in valores if v > media_faturamento)

print(f"Menor faturamento: R${menor_valor:.2f}")
print(f"Maior faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
