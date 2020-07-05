
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CBRACKET EQUAL MINUS NUMBER OBRACKET PLUS nl\n        expr_list : expr_list expr\n                    | expr\n        \n        expr : e EQUAL\n        \n        e : e PLUS t\n            | e MINUS t\n            | t\n        \n        t : OBRACKET e CBRACKET\n                | NUMBER\n        '
    
_lr_action_items = {'OBRACKET':([0,1,2,5,7,8,9,10,],[5,5,-2,5,-1,-3,5,5,]),'NUMBER':([0,1,2,5,7,8,9,10,],[6,6,-2,6,-1,-3,6,6,]),'$end':([1,2,7,8,],[0,-2,-1,-3,]),'EQUAL':([3,4,6,12,13,14,],[8,-6,-8,-4,-5,-7,]),'PLUS':([3,4,6,11,12,13,14,],[9,-6,-8,9,-4,-5,-7,]),'MINUS':([3,4,6,11,12,13,14,],[10,-6,-8,10,-4,-5,-7,]),'CBRACKET':([4,6,11,12,13,14,],[-6,-8,14,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expr_list':([0,],[1,]),'expr':([0,1,],[2,7,]),'e':([0,1,5,],[3,3,11,]),'t':([0,1,5,9,10,],[4,4,4,12,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expr_list","S'",1,None,None,None),
  ('expr_list -> expr_list expr','expr_list',2,'p_expr_list','myParser.py',27),
  ('expr_list -> expr','expr_list',1,'p_expr_list','myParser.py',28),
  ('expr -> e EQUAL','expr',2,'p_expr','myParser.py',33),
  ('e -> e PLUS t','e',3,'p_e','myParser.py',40),
  ('e -> e MINUS t','e',3,'p_e','myParser.py',41),
  ('e -> t','e',1,'p_e','myParser.py',42),
  ('t -> OBRACKET e CBRACKET','t',3,'p_t','myParser.py',47),
  ('t -> NUMBER','t',1,'p_t','myParser.py',48),
]