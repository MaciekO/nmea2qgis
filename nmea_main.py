# -*- coding: utf-8 -*-
"""
/***************************************************************************
 nmea_main
                                 A QGIS plugin

This plugin loads nmea data into QGIS. It supports GGA, GLL and RMC sentences.
You can also choose to write the data on disk as a shapefile.

                              -------------------
        begin                : 2013-05-11
        copyright            : (C) 2013 by Maciej Olszewski
        email                : mackoo@opoczta.pl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources
from nmea_dialog import nmea_mainDialog,nmea_settDialog
import time,os,string

class nmea_main:

    def __init__(self, iface):
        self.iface = iface
        self.dlg = nmea_mainDialog()
        self.dlg3=nmea_settDialog()

        QObject.connect(self.dlg.ui.pushButton,SIGNAL("clicked()"), self.dialog)
        QObject.connect(self.dlg.ui.ButExit,SIGNAL("clicked()"), self.exit)
        QObject.connect(self.dlg.ui.addBut,SIGNAL("clicked()"), self.addLayer)
        QObject.connect(self.dlg.ui.settBut,SIGNAL("clicked()"), self.sett)

    def initGui(self):
        self.action = QAction(
            QIcon(":/plugins/nmea_main/icon.png"),
            u"nmea2qgis", self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&nmea2qgis", self.action)
        self.fd = QFileDialog()
        self.fd1 = QFileDialog()
        settings=QSettings()
        try:
            dir=settings.value('/nmea2qgis/dir', 'C:\Users')
            self.fd.setDirectory(dir)
        except:
            pass

    def unload(self):
        self.iface.removePluginMenu(u"&nmea2qgis", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        self.dlg.show()

    def dialog(self):
        self.filenames = self.fd.getOpenFileNames(None,"","","all (*.*);;nmea (*.nmea)")
        if len(self.filenames)<>0:
            from os.path import isfile
            if isfile(self.filenames[0]):

                self.dlg.ui.lineEdit.setText(self.filenames[0])
                settings=QSettings()
                settings.setValue('/nmea2qgis/dir',self.filenames[0])
                self.fd.setDirectory(os.path.dirname(str(self.filenames[0])))


    def exit(self):
        self.dlg.close()
        self.dlg.ui.lineEdit.setText("")


    def sett(self):
        self.dlg3.show()


    def addLayer(self):

        for filename in self.filenames:
##            try:
                nmeafile=open(filename)
                self.nmeaDict(nmeafile)
                self.addSave(filename)
##            except:
##                if self.dlg.ui.lineEdit.text()=='': QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot add nmealayer, \ncheck the file path")
##                else:   QMessageBox.information(self.iface.mainWindow(), "Info", "Cannot add nmealayer")

    def nmeaDict(self,nmeafile):
        self.nl=self.dlg3.ui.nullBox.value()
        nl=self.nl
        self.nmeadict={}
        nmeafile.seek(0)
        self.dlg.close()
        for line in nmeafile:
             linee=line.split(',')
             if line[3:6]=='GGA' or line[3:6]=='RMC':
                 self.nmeadict[linee[1]]=['',nl,nl,nl,nl,nl,nl,nl,nl,nl,nl]
             if line[3:6]=='GLL':
                 self.nmeadict[linee[5]]=['',nl,nl,nl,nl,nl,nl,nl,nl,nl,nl]

        nmeafile.seek(0)
        for line in nmeafile:
            if line[3:6]=='GGA' or line[3:6]=='GLL' or line[3:6]=='RMC':
                try:
                    parser={'GGA':self.par_gga,'RMC':self.par_rmc,'GLL':self.par_gll}[line[3:6]]
                    parser(line)
                except:
                    QMessageBox.critical(self.iface.mainWindow(), 'error', "problem parsing line:  "+line)
                    break



        nmeafile.close()

        self.utc=[]
        self.lat=[]
        self.lon=[]
        self.numSV=[]
        self.hdop=[]
        self.msl=[]
        self.geoid=[]
        self.speed=[]
        self.fixstatus=[]
        self.datastatus=[]

        for keyy in self.nmeadict.keys():
            self.utc.append(self.nmeadict[keyy][0])
            self.numSV.append((self.nmeadict[keyy][3]))
            self.hdop.append((self.nmeadict[keyy][4]))
            self.lon.append(self.nmeadict[keyy][2])
            self.lat.append(self.nmeadict[keyy][1])
            self.msl.append((self.nmeadict[keyy][5]))
            self.geoid.append((self.nmeadict[keyy][6]))
            self.speed.append((self.nmeadict[keyy][7]))
            self.fixstatus.append(int(self.nmeadict[keyy][9]))
            self.datastatus.append(self.nmeadict[keyy][10])




    def addSave(self,filename):
        import ntpath
        try:
            layername=ntpath.basename(str(filename))

        except:
            layername="nmealayer"


        self.epsg4326= QgsCoordinateReferenceSystem()
        self.epsg4326.createFromString("epsg:4326")
        nmealayer = QgsVectorLayer("Point?crs=epsg:4326", layername, "memory")
        nmealayer.startEditing()

        pr = nmealayer.dataProvider()
        att=[]
        a=0
        if self.dlg3.ui.latCheck.isChecked():
               pr.addAttributes( [ QgsField("latitude", QVariant.Double)] )
               att.append(self.lat)
               a+=1
        if self.dlg3.ui.lonCheck.isChecked():
               pr.addAttributes( [ QgsField("longitude", QVariant.Double)] )
               att.append(self.lon)
               a+=1
        if self.dlg3.ui.utcCheck.isChecked():
               pr.addAttributes( [ QgsField("utc", QVariant.String)] )
               att.append(self.utc)
               a+=1
        if self.dlg3.ui.svCheck.isChecked():
               pr.addAttributes( [ QgsField("numSV", QVariant.Double)] )
               att.append(self.numSV)
               a+=1
        if self.dlg3.ui.hdopCheck.isChecked():
               pr.addAttributes( [ QgsField("hdop", QVariant.Double)] )
               att.append(self.hdop)
               a+=1
        if self.dlg3.ui.mslCheck.isChecked():
               pr.addAttributes( [ QgsField("msl", QVariant.Double)] )
               att.append(self.msl)
               a+=1
        if self.dlg3.ui.geoidCheck.isChecked():
               pr.addAttributes( [ QgsField("geoid", QVariant.Double)] )
               att.append(self.geoid)
               a+=1
        if self.dlg3.ui.speedCheck.isChecked():
               pr.addAttributes( [ QgsField("speed", QVariant.Double)] )
               att.append(self.speed)
               a+=1
        if self.dlg3.ui.fixstatusCheck.isChecked():
               pr.addAttributes( [ QgsField("fixstatus", QVariant.Double)] )
               att.append(self.fixstatus)
               a+=1
        if self.dlg3.ui.datastatusCheck.isChecked():
               pr.addAttributes( [ QgsField("datastatus", QVariant.Double)] )
               att.append(self.datastatus)
               a+=1



        fett=[]
        for a,lat in enumerate(self.lat):
            fet = QgsFeature()
            fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(self.lon[a],lat)))
            attributess=[]
            for aa in att:
                attributess.append(aa[a])
            fet.setAttributes(attributess)
            fett.append(fet)


        pr.addFeatures(fett)

        nmealayer.commitChanges()
        nmealayer.updateExtents()
        QgsMapLayerRegistry.instance().addMapLayer(nmealayer)
        if self.dlg3.ui.saveCheck.isChecked():
            self.filename = self.fd.getSaveFileName()
            error = QgsVectorFileWriter.writeAsVectorFormat(nmealayer, self.filename, "CP1250", self.epsg4326, "ESRI Shapefile")

        self.iface.mapCanvas().zoomToFullExtent()


    def par_gga(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        if data[3]=='N':
            latt=float(data[2][:2])+float(data[2][2:])/60
        elif data[3]=='S':
            latt=-1*float(data[2][:2])-float(data[2][2:])/60
        else:
            latt=self.nl
        ind=string.find(data[4],".")
        if data[5]=='E':
            lonn=float(data[4][:(ind-2)])+float(data[4][(ind-2):])/60
        elif data[5]=='W':
            lonn=-1*float(data[4][:(ind-2)])-float(data[4][(ind-2):])/60
        else:
            lonn=self.nl
        try:    numsv=float(data[7])
        except: numsv=self.nl
        try:    hdop=float(data[8])
        except: hdop=self.nl
        try:    msl=float(data[9])
        except: msl=self.nl
        try:    geoid=float(data[11])
        except: geoid=self.nl
        try:    fixstatus=float(data[6])
        except: fixstatus=self.nl

        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][3]=numsv
        self.nmeadict[key][4]=hdop
        self.nmeadict[key][5]=msl
        self.nmeadict[key][6]=geoid
        self.nmeadict[key][9]=fixstatus

    def par_rmc(self,line):
        data=[]
        data=line.split(',')
        key=data[1]
        utc=data[1][:2]+':'+data[1][2:4]+':'+data[1][4:6]
        if data[4]=='N':
            latt=float(data[3][:2])+float(data[3][2:])/60
        elif data[4]=="S":
            latt=-1*float(data[3][:2])-float(data[3][2:])/60
        else:
            latt=self.nl
        ind=string.find(data[5],".")
        if data[6]=='E':
            lonn=float(data[5][:(ind-2)])+float(data[5][(ind-2):])/60
        elif data[6]=='W':
            lonn=-1*float(data[5][:(ind-2)])-float(data[5][(ind-2):])/60
        else:
            lonn=self.nl
        try:    speed=float(data[7])
        except: speed=self.nl
        try:
            if data[2]=='A':    datastatus=1
            else:   datastatus=0
        except: datastatus=self.nl

        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][7]=speed
        self.nmeadict[key][10]=datastatus

    def par_gll(self,line):
        data=[]
        data=line.split(',')
        key=data[5]
        utc=data[5][:2]+':'+data[5][2:4]+':'+data[5][4:6]
        if data[2]=='N':
            latt=float(data[1][:2])+float(data[1][2:])/60
        elif data[2]=='S':
            latt=-1*float(data[1][:2])-float(data[1][2:])/60
        else:
            latt=self.nl
        ind=string.find(data[3],".")
        if data[4]=='E':
            lonn=float(data[3][:(ind-2)])+float(data[3][(ind-2):])/60
        elif data[4]=='W':
            lonn=-1*float(data[3][:(ind-2)])-float(data[3][(ind-2):])/60
        else:
            lonn=self.nl
        try:
            if data[6]=='A':    datastatus=1
            else:   datastatus=0
        except: datastatus=self.nl

        self.nmeadict[key][0]=utc
        self.nmeadict[key][1]=latt
        self.nmeadict[key][2]=lonn
        self.nmeadict[key][10]=datastatus



