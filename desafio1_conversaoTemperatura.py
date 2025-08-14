def converteUnidade(entrada:str) -> str:
  if not isinstance(entrada, str):
    raise TypeError('A unidade deve ser do tipo str.')
  if entrada.lower() in ['celsius', 'c']:
    return 'C'
  if entrada.lower() in ['fahrenheit', 'f']:
    return 'F'
  if entrada.lower() in ['kelvin', 'k']:
    return 'K'
  raise ValueError('A unidade não é permitida.')

def verificaNumero(entrada) -> bool:
  if isinstance(entrada, int) or isinstance(entrada, float):
    return True
  if isinstance(entrada, str):
    caracteres = entrada.split('')
    for caracter in caracteres:
      try:
        pass
  

def converter(valor, de, para) -> float:
  de, para = converteUnidade(de), converteUnidade(para)
  if not isinstance(valor, float):
    raise TypeError('O valor deve ser um número, cujos decimais são separados por ponto.')
  if de == para:
    raise ValueError('A conversão deve ser entre unidades de medida diferentes.')
  if verificaNumero(valor):
    if de == 'C':
      if valor < -273.15:
        raise ValueError('A escala Celsius não admite valores menores que -273,15ºC')
      if para == 'F':
        print f'{valor * 9/5 + 32:.2f}'
      if para == 'K':
        return valor + 273.15
    if de == 'F':
      pass
  
  
  
