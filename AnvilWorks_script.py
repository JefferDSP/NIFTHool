from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    seq_coming_from_anvil= self.Your_Sequence.text
    predic, p0, p1, list_similit= anvil.server.call('function_pred_seq',seq_coming_from_anvil)
    print('...')
    'FIRST, the function' 'SECOND, the parameter for function'
    
    self.label_3.text= f'Prediction is: Your {predic}'
    if predic == 'sequence is related to nifh':
      self.label_4.text= f'Percentage accuracy: {p1}'
    else:
      if p0 > 85:
        self.label_4.text= f'Percentage accuracy: {p0}'
    
    if len(list_similit) >= 1:
      self.label_7.text= f'This sequence was found in {len(list_similit)} sequences of database'
      for t in list_similit:
        self.label_5.text= f'Your sequence was found in the organism: {t[1]}'
        self.label_6.text= f'In its sequence: {t[2]}'

    else:
      self.label_5.text= f'This sequence is NOT FOUND in the database of nifh'
    
    pass

  def Your_Sequence_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
