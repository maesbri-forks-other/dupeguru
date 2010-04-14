# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2010-04-12
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from qtlib.column import Column
from qtlib.table import Table
from core.gui.problem_table import ProblemTable as ProblemTableModel

class ProblemTable(Table):
    COLUMNS = [
        Column('path', 'File Path', 150),
        Column('msg', 'Error Message', 150),
    ]
    
    def __init__(self, problem_dialog, view):
        model = ProblemTableModel(view=self, problem_dialog=problem_dialog.model)
        Table.__init__(self, model, view)
        # we have to prevent Return from initiating editing.
        # self.view.editSelected = lambda: None
    