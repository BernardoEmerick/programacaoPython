from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional

@dataclass
class Servico:
  id: int
  nome: str
  pai: Optional['Servico'] = None
  descricao: Optional[str] = None
  filhos: List['Servico'] = field(default_factory=list, repr=False)

  def set_pai(self, novo_pai = Optional['Servico']) -> None:
    if novo_pai is self:
      raise ValueError('Um serviço não pode ser seu próprio pai.')
    # Chaca se ocorre um ciclo
    anc = novo_pai
    while anc is not None:
      if anc is self:
        raise ValueError('Ciclo detectado na hierarquia de serviços.')
      anc = anc.pai
    #Exclui o serviço da lista dos filhos do seu pai anterior
    self.pai.filhos.remove(self)
    self.pai = novo_pai
    if novo_pai is not None and self not in novo_pai.filhos:
      novo_pai.filhos.append(self)

@dataclass
class Setor:
  id: int
  nome: str
  sigla: Optional[str] = None
  pai: Optional[Setor] = None
  filhos: List['Setor'] = field(default_factory=list, repr=False)

  def set_pai(self, novo_pai: Optional['Setor']) -> None:
    if novo_pai is self:
      raise ValueError('Um setor não pode ser seu próprio pai')
    # Checa se ocorre um ciclo
    anc = novo_pai
    while anc is not None:
      if anc is self:
        raise ValueError('Ciclo detectado na hierarquia de setores')
      anc = anc.pai
    # Exclui da lista dos filhos do pai anterior
    if self.pai is not None:
      self.pai.filhos.remove(self)
    self.pai = novo_pai
    # Coloca o setor na lista de filhos do novo pai
    if novo_pai is not None and self not in novo_pai.filhos:
      novo_pai.filhos.append(self)

  def caminho(self) -> List['Setor']:
    # Retorna a cadeia de ancestrais até a raiz (inclusive o próprio setor).
    seq, atual = [], self
    while atual:
      seq.append(atual)
      atual = atual.pai
    return list(reversed(seq)) #raiz -> ... -> self
