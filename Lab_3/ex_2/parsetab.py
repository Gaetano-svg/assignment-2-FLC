
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARROW AV BO CL CM DATE INT ISBN LETTER LI LS NAME S SEP SO nl\n        file : authors_list SEP loans_list\n        \n        authors_list : authors_list author_entry \n                        | author_entry\n        \n        author_entry : NAME ARROW books S\n        \n        books : books CM book \n                | book\n        \n        book : ISBN CL NAME CL INT CL collocation \n                | ISBN CL NAME CL INT\n        \n        collocation : l_g INT LETTER \n                        | l_g INT\n        \n        l_g : LI AV \n                | LI SO \n                | LS AV \n                | LS SO \n                | LS BO\n        \n        loans_list : loans_list loan_entry \n                        | loan_entry\n        \n        loan_entry : NAME CL loan_books S\n        \n        loan_books : loan_books CM DATE ISBN \n                        | DATE ISBN\n        \n        empty :\n        '
    
_lr_action_items = {'NAME':([0,2,3,5,6,8,9,14,16,18,23,],[4,4,-3,10,-2,10,-17,-16,-4,22,-18,]),'$end':([1,8,9,14,23,],[0,-1,-17,-16,-18,]),'SEP':([2,3,6,16,],[5,-3,-2,-4,]),'ARROW':([4,],[7,]),'ISBN':([7,17,20,27,],[13,13,25,29,]),'CL':([10,13,22,28,],[15,18,26,30,]),'S':([11,12,19,21,25,28,29,31,35,41,],[16,-6,23,-5,-20,-8,-19,-7,-10,-9,]),'CM':([11,12,19,21,25,28,29,31,35,41,],[17,-6,24,-5,-20,-8,-19,-7,-10,-9,]),'DATE':([15,24,],[20,27,]),'INT':([26,32,36,37,38,39,40,],[28,35,-11,-12,-13,-14,-15,]),'LI':([30,],[33,]),'LS':([30,],[34,]),'AV':([33,34,],[36,38,]),'SO':([33,34,],[37,39,]),'BO':([34,],[40,]),'LETTER':([35,],[41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'file':([0,],[1,]),'authors_list':([0,],[2,]),'author_entry':([0,2,],[3,6,]),'loans_list':([5,],[8,]),'loan_entry':([5,8,],[9,14,]),'books':([7,],[11,]),'book':([7,17,],[12,21,]),'loan_books':([15,],[19,]),'collocation':([30,],[31,]),'l_g':([30,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> file","S'",1,None,None,None),
  ('file -> authors_list SEP loans_list','file',3,'p_file','parser.py',21),
  ('authors_list -> authors_list author_entry','authors_list',2,'p_authors_list','parser.py',28),
  ('authors_list -> author_entry','authors_list',1,'p_authors_list','parser.py',29),
  ('author_entry -> NAME ARROW books S','author_entry',4,'p_author_entry','parser.py',34),
  ('books -> books CM book','books',3,'p_books','parser.py',39),
  ('books -> book','books',1,'p_books','parser.py',40),
  ('book -> ISBN CL NAME CL INT CL collocation','book',7,'p_book','parser.py',45),
  ('book -> ISBN CL NAME CL INT','book',5,'p_book','parser.py',46),
  ('collocation -> l_g INT LETTER','collocation',3,'p_collocation','parser.py',51),
  ('collocation -> l_g INT','collocation',2,'p_collocation','parser.py',52),
  ('l_g -> LI AV','l_g',2,'p_lg','parser.py',57),
  ('l_g -> LI SO','l_g',2,'p_lg','parser.py',58),
  ('l_g -> LS AV','l_g',2,'p_lg','parser.py',59),
  ('l_g -> LS SO','l_g',2,'p_lg','parser.py',60),
  ('l_g -> LS BO','l_g',2,'p_lg','parser.py',61),
  ('loans_list -> loans_list loan_entry','loans_list',2,'p_loans_list','parser.py',66),
  ('loans_list -> loan_entry','loans_list',1,'p_loans_list','parser.py',67),
  ('loan_entry -> NAME CL loan_books S','loan_entry',4,'p_loan_entry','parser.py',72),
  ('loan_books -> loan_books CM DATE ISBN','loan_books',4,'p_loan_books','parser.py',77),
  ('loan_books -> DATE ISBN','loan_books',2,'p_loan_books','parser.py',78),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',86),
]
