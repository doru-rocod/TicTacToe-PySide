#xSi0.py

#coding: UTF-16
import os
import subprocess
import itertools
import sys
from PySide.QtGui import * 
from PySide.QtCore import *


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 
class Tabel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("X si 0")
        self.setGeometry(300, 200, 302, 364)
        #self.setSizeHint(302, 364)
        colcnt = len(data[0])
        rowcnt = len(data)
        self.tabel = QTableWidget(rowcnt, colcnt)
        self.tabel.horizontalHeader().hide()
        self.tabel.verticalHeader().hide()
        self.mutariom = []
        self.mutariramase = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.mutaricalc = []
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(60)
        self.tabel.setFont(font)

        for row in range(rowcnt):
            self.tabel.setRowHeight(row, 100)
          
        for i in range(rowcnt):
            for j in range(colcnt):
                item = QTableWidgetItem()
                item.setTextAlignment(5)
                self.tabel.setItem(i, j, item)


      
        self.setCentralWidget(self.tabel)
        self.statusBar().showMessage("Jocul a inceput. Omul muta primul.", 3000)

        restartAction = QAction(QIcon('res3.png'), 'Restart', self)
        restartAction.setShortcut('Ctrl+R')
        restartAction.triggered.connect(self.restartJoc)

        exitAction = QAction(QIcon('exit1.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(self.exitJoc)
        
        self.toolbar = self.addToolBar('Restart')
        self.toolbar.addAction(restartAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exitAction)
        
        
        
              
        self.unu = self.tabel.item(0, 0)
        self.doi = self.tabel.item(0, 1)
        self.trei = self.tabel.item(0, 2)
        self.patru = self.tabel.item(1, 0)
        self.cinci = self.tabel.item(1, 1)
        self.sase = self.tabel.item(1, 2)
        self.sapte = self.tabel.item(2, 0)
        self.opt = self.tabel.item(2, 1)           
        self.noua = self.tabel.item(2, 2)

        self.items = [self.tabel.item(0, 0), self.tabel.item(0, 1), self.tabel.item(0, 2),
                      self.tabel.item(1, 0), self.tabel.item(1, 1), self.tabel.item(1, 2),
                      self.tabel.item(2, 0), self.tabel.item(2, 1), self.tabel.item(2, 2)]

        self.incoltiri = {((0, 1), (1, 2)):(0, 2),
                          ((1, 2), (0, 1)):(0, 2), 
                          ((1, 2), (2, 1)):(2, 2),
                          ((2, 1), (1, 2)):(2, 2), 
                          ((2, 1), (1, 0)):(2, 0),
                          ((1, 0), (2, 1)):(2, 0), 
                          ((1, 0), (0, 1)):(0, 0),
                          ((0, 1), (1, 0)):(0, 0),
                          ((0, 2), (2, 1)):(2, 2),
                          ((2, 1), (0, 2)):(2, 2), 
                          ((2, 1), (0, 0)):(2, 0),
                          ((0, 0), (2, 1)):(2, 0), 
                          ((1, 0), (0, 2)):(0, 0),
                          ((0, 2), (1, 0)):(0, 0), 
                          ((0, 1), (2, 2)):(0, 2),
                          ((2, 2), (0, 1)):(0, 2),
                          ((1, 2), (2, 0)):(2, 2),
                          ((2, 0), (1, 2)):(2, 2),
                          ((2, 2), (1, 0)):(2, 0),
                          ((1, 0), (2, 2)):(2, 0),
                          ((2, 0), (0, 1)):(0, 0),
                          ((0, 1), (2, 0)):(0, 0),
                          ((0, 0), (1, 2)):(0, 2),
                          ((1, 2), (0, 0)):(0, 2)}
                             
        self.mijloaceOpuse = [[(0, 1), (2, 1)], [(1, 2), (1, 0)]]
        self.colturi = [(0,0), (0, 2), (2,0), (2, 2)]
        self.mijloace = [(0,1), (1, 2), (2, 1), (1,0)]
        self.varianteWin = [
                       [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                       [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                       [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]
                      ]
        #conectarea click-ului la functia principala
        self.tabel.cellClicked.connect(self.functiaPrincipala)
        


     #fct in care se deruleaza jocul in functie de nr de mutari facute ale omului   
    def functiaPrincipala(self, a, b):
        self.tabel.item(a, b).setText("x")
        rowcolmutom = (a, b)
        self.mutariom.append(rowcolmutom)
        self.mutariramase.remove(rowcolmutom) 
        if len(self.mutariom) == 1:
            if self.mutariom[0] == (1,1):
                self.unu.setText("o")
                self.mutaricalc.append((0, 0))
                self.mutariramase.remove((0, 0))
            else:
                self.cinci.setText("o")
                self.mutariramase.remove((1, 1))
                self.mutaricalc.append((1, 1))
        elif len(self.mutariom) == 2:
            #t = self.verVarianteWinOm()
            t = self.verVarianteWin(self.varianteWin, self.mutariom, self.mutariramase, self.mutaricalc)
            if t:
                #daca omul are vreo varianta de castig imediat calculatorul pune acolo
                self.tabel.item(t[0], t[1]).setText("o")
                #self.mutariramase.remove(t)
            else:
                #daca calc are pus in centru 
                if (1,1) in self.mutaricalc:
                    i = self.verIncoltiri()
                    if i:
                        self.tabel.item(i[0], i[1]).setText("o")
                        self.mutaricalc.append((i[0], i[1]))
                        self.mutariramase.remove(i)
                    else:
                        for i in self.mijloace:
                            if i not in self.mutariom and i in self.mutariramase:
                                self.tabel.item(i[0], i[1]).setText("o")
                                self.mutaricalc.append((i[0], i[1]))
                                self.mutariramase.remove((i[0], i[1]))
                                break
                else:
                    self.tabel.item(2, 0).setText("o")
                    self.mutaricalc.append((2, 0))
                    self.mutariramase.remove((2, 0))
        elif len(self.mutariom) == 3:
            v = self.verVarianteWin(self.varianteWin, self.mutaricalc, self.mutariramase, self.mutariom)
            if v:
                self.tabel.item(v[0], v[1]).setText("o")
                check, litera = self.verWin()
            else:
                vv = self.verVarianteWin(self.varianteWin, self.mutariom, self.mutariramase, self.mutaricalc)
                if vv:
                    self.tabel.item(vv[0], vv[1]).setText("o")
                else:
                    for i in self.colturi:
                        if i in self.mutariramase:
                            self.tabel.item(i[0], i[1]).setText("o")
                            self.mutaricalc.append((i[0], i[1]))
                            self.mutariramase.remove((i[0], i[1]))
                            break
        elif len(self.mutariom) == 4:
            v = self.verVarianteWin(self.varianteWin, self.mutaricalc, self.mutariramase, self.mutariom)
            if v:
                self.tabel.item(v[0], v[1]).setText("o")
                check, litera = self.verWin()
            else:
                vv = self.verVarianteWin(self.varianteWin, self.mutariom, self.mutariramase, self.mutaricalc)
                if vv:
                    self.tabel.item(vv[0], vv[1]).setText("o")
                else:
                    for i in self.colturi:
                        if i in self.mutariramase:
                            self.tabel.item(i[0], i[1]).setText("o")
                            self.mutaricalc.append((i[0], i[1]))
                            self.mutariramase.remove((i[0], i[1]))
                            break
                        else:
                            for i in self.mutariramase:
                                self.tabel.item(i[0], i[1]).setText("o")
                                self.mutaricalc.append((i[0], i[1]))
                                self.mutariramase.remove((i[0], i[1]))
                            break
        if len(self.mutariramase) == 0:
            self.statusBar().showMessage("Jocul s-a terminat remiza")
            

    #fct care verifica daca exista vreo incoltire si da mutarea contra ei
    def verIncoltiri(self):
        t = tuple(self.mutariom)
        mutare = self.incoltiri.get(t)
        if mutare:
            return (mutare[0], mutare[1])
        else:
            return False
    #fct care verifica daca exista variante de castig imediat  
    def verVarianteWin(self, listavarwin, listavarplayer, listavarramase, listavaradversar):
        listavarplayer = [list(x) for x in itertools.combinations(listavarplayer, 2)]
        for i in listavarwin:
            for j in listavarplayer:
                if (j[0] in i) and (j[1] in i):
                    for k in i:
                        if k not in listavarplayer and k in listavarramase and k not in listavaradversar:
                            self.mutaricalc.append((k[0], k[1]))
                            listavarramase.remove((k[0], k[1]))
                            return (k[0], k[1])


    #vedem daca omul a pus in doua mijloace ca sa incolteasca la urmatoare mutare
    def nuDouaMijloace(self):
        for i in self.mutariom:
            if i not in self.mijloace:
                return True

    #fct care verifica daca calc a castigat si daca da, slecteaza campurile castigatoare si deselecteaza campul ultimei mutari
    def verWin(self):
        if (self.unu.text() == self.doi.text() == self.trei.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.unu.setSelected(True)
            self.doi.setSelected(True)
            self.trei.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.unu.text()
        elif (self.patru.text() == self.cinci.text() == self.sase.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.patru.setSelected(True)
            self.cinci.setSelected(True)
            self.sase.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.patru.text()
        elif (self.sapte.text() == self.opt.text() == self.noua.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.sapte.setSelected(True)
            self.opt.setSelected(True)
            self.noua.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.sapte.text()
        elif (self.unu.text() == self.patru.text() == self.sapte.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.unu.setSelected(True)
            self.patru.setSelected(True)
            self.sapte.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.unu.text()
        elif (self.doi.text() == self.cinci.text() == self.opt.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.doi.setSelected(True)
            self.cinci.setSelected(True)
            self.opt.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.doi.text()
        elif (self.trei.text() == self.sase.text() == self.noua.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.trei.setSelected(True)
            self.sase.setSelected(True)
            self.noua.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.trei.text()
        elif (self.unu.text() == self.cinci.text() == self.noua.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.unu.setSelected(True)
            self.cinci.setSelected(True)
            self.noua.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.unu.text()
        elif (self.trei.text() == self.cinci.text() == self.sapte.text() != ''):
            for i in self.items:
                if i.isSelected():
                    i.setSelected(False)
            self.trei.setSelected(True)
            self.cinci.setSelected(True)
            self.sapte.setSelected(True)
            self.statusBar().showMessage("Calculatorul a castigat!")
            return True, self.trei.text()
        else:
            return False

    def restartJoc(self):
        self.close()
        subprocess.call("python" + " TicTacToe.py", shell=True)

    def exitJoc(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    widget = Tabel()
    widget.show()
    widget.raise_()
    sys.exit(app.exec_())
        
    
 
if __name__ == "__main__":
    main()
