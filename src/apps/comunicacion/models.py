# -*- coding: utf-8 -*-
from django.db import models
from usuario.models import Organismo
from ubigeo.models import Region, Provincia

AUDITORIA = (
        (1,'ACTIVO'),
        (2,'ELIMINADO'),
        )

class Oac(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    numoac = models.IntegerField(verbose_name='Numero de la oac', unique=True)
    organismo = models.ForeignKey(Organismo, verbose_name='Organismo')
    dependencia = models.IntegerField(verbose_name='Dependencia',)
    archivo = models.FileField(upload_to='oac/',verbose_name='Adjuntar Archivo',)
    urloac = models.URLField(verbose_name='Url de la oac',max_length=70,null=True,blank=True)
    idusuario_creac = models.IntegerField(verbose_name='Usuario creador',)
    fec_creac = models.DateTimeField(verbose_name='Fecha de creación del registro',auto_now_add=True)

    class Meta:
        db_table = u'oac'
        verbose_name = u'Organigrama de Área de Comunicaciones'
        verbose_name_plural = u'Organigramas del Área de Comunicaciones'

    def __unicode__(self):
        return self.urloac

class TipoOgcs(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nombre = models.CharField(verbose_name='Nombre del tipoogcs',max_length=15)
    
    class Meta:
        db_table = u'tipoogcs'
        verbose_name = u'Tipo Ogcs'
        verbose_name_plural = u'Tipos de Ogcs'

    def __unicode__(self):
        return self.nombre

class Pgcs(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    numpgcs = models.IntegerField(verbose_name='Numero de la pgcs',unique=True)
    organismo = models.ForeignKey(Organismo, verbose_name='Organismo')
    dependencia = models.IntegerField(verbose_name='Dependencia',)
    archivo = models.FileField(upload_to='pgcs/',verbose_name='Adjuntar Archivo',)
    urlpgcs = models.URLField(verbose_name='Url de la pgcs', max_length=70)
    tipopgcs = models.ForeignKey(TipoOgcs,verbose_name='Estado del tipo de pgcs')
    idusuario_creac = models.IntegerField(verbose_name='Usuario creador',)
    fec_creac = models.DateTimeField(verbose_name='Fecha de creación del registro',auto_now_add=True)
    
    class Meta:
        db_table = u'pgcs'
        verbose_name = u'Plan General de Comunicación del sector'
        verbose_name_plural = u'Planes Generales de Comunicación del sector'

    def __unicode__(self):
        return self.nombre

class MccaTipoComunicacion(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nombre = models.CharField(verbose_name='Nombre del MccaTipoComunicacion',max_length=50)
    
    class Meta:
        db_table = u'mccatipocomunicacion'
        verbose_name = u'Matriz de Campaña de Comunicaciones Año'
        verbose_name_plural = u'Matrices de Campaña de Comunicaciones Anuales'

    def __unicode__(self):
        return self.nombre

class Mcca(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nummcca = models.IntegerField(verbose_name='Numero de la mcca', unique=True)
    nombremmca = models.CharField(verbose_name='Nombre de la mmca',max_length=70)
    fechaini = models.DateTimeField(verbose_name='Fecha de inicio de la campaña',)
    fechafin = models.DateTimeField(verbose_name='Fecha de final de la campaña',)	
    publico = models.TextField(verbose_name='Nombre del público objetivo',)
    idusuario_creac = models.IntegerField(verbose_name='Usuario creador',)
    fec_creac = models.DateTimeField(verbose_name='Fecha de creación del registro',auto_now_add=True)
    idusuario_mod = models.IntegerField(verbose_name='Usuario modifico', null=True, blank=True)
    fec_mod = models.DateTimeField(verbose_name='Fecha modifico', auto_now=True, null=True, blank=True)
    idadministrador_mod	= models.IntegerField(verbose_name='Usuario modifico', null=True, blank=True)
    fec_modadm = models.DateTimeField(verbose_name='Fecha modifico', auto_now=True, null=True, blank=True)

    class Meta:
        db_table = u'mcca'
        verbose_name = u'mcca tipo'
        verbose_name_plural = u'mcca tipos'

    def __unicode__(self):
        return self.nombremmca


class MccaEstado(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    organismo = models.ForeignKey(Organismo, verbose_name='Organismo')
    dependencia = models.IntegerField(verbose_name='Dependencia',)

    class Meta:
        db_table = u'mccaestado'
        verbose_name = u'MCCA estado'
        verbose_name_plural = u'MCCA estado'

    def __unicode__(self):
        return self.nummcca

class MccaPrivado(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    privado = models.CharField(verbose_name='Nombre de los sectores involucrados', max_length=150)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccaprivado'
        verbose_name = u'MCCA privado'
        verbose_name_plural = u'MCCA privado'

    def __unicode__(self):
        return self.privado

class MccaIndicador(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    indicador = models.CharField(verbose_name='Nombre de los indicadores', max_length=300)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccaindicador'
        verbose_name = u'MCCA Indicador'
        verbose_name_plural = u'MCCA Indicador'

    def __unicode__(self):
        return self.indicador


class MccaMensaje(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    mensaje = models.CharField(verbose_name='Nombre de los indicadores', max_length=300)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccamensaje'
        verbose_name = u'MCCA Mensaje'
        verbose_name_plural = u'MCCA Mensaje'

    def __unicode__(self):
        return self.mensaje


class MccaCanal(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    tipommca = models.ForeignKey(MccaTipoComunicacion, verbose_name='Mcca Tipo Comunicacion',)
    canal = models.CharField(verbose_name='Nombre del canal de comunicacion', max_length=300)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccacanal'
        verbose_name = u'MCCA Canal'
        verbose_name_plural = u'MCCA Canal'

    def __unicode__(self):
        return self.canal


class MccaAccion(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)
    fechaini = models.DateTimeField(verbose_name='Fecha de inicio de la acciones planteadas')
    fechafin = models.DateTimeField(verbose_name='Fecha final de la campaña')
    acciones = models.CharField(verbose_name='Nombre de las acciones planteadas',max_length=200)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccaaccion'
        verbose_name = u'MCCA Accion'
        verbose_name_plural = u'MCCA Accion'

    def __unicode__(self):
        return self.acciones


class MccaObservacion(models.Model):
    nummcca = models.ForeignKey(Mcca,verbose_name='Codigo mcca',to_field='nummcca')
    item = models.IntegerField(verbose_name='Items',)    
    observacion = models.CharField(verbose_name='Nombre del canal de comunicacion', max_length=300)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccaobservacion'
        verbose_name = u'MCCA Observacion'
        verbose_name_plural = u'MCCA Observacion'

    def __unicode__(self):
        return self.observacion

class MccTipo(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nombre = models.CharField(verbose_name='Nombre del tipoogcs',max_length=50)
    
    class Meta:
        db_table = u'mcctipo'
        verbose_name = u'mcc tipo'
        verbose_name_plural = u'mcc tipos'

    def __unicode__(self):
        return self.nombre

class MccEstado(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nombre = models.CharField(verbose_name='Nombre del tipoogcs',max_length=15)
    
    class Meta:
        db_table = u'mccestado'
        verbose_name = u'mcc estado'
        verbose_name_plural = u'mcc estados'

    def __unicode__(self):
        return self.nombre

class MccTipoVarios(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nombre = models.CharField(verbose_name='Nombre del tipoogcs',max_length=15)
    
    class Meta:
        db_table = u'mcctipovarios'
        verbose_name = u'mcc tipo varios'
        verbose_name_plural = u'mcc tipos varios'

    def __unicode__(self):
        return self.nombre


class Mcc(models.Model):
    codigo = models.AutoField(verbose_name='Codigo Autoincrementado',primary_key=True)
    nummcc = models.IntegerField(verbose_name='Numero de la mcc', unique=True)
    nombremmc = models.CharField(verbose_name='Nombre de la mmca',max_length=120)
    fechaini = models.DateTimeField(verbose_name='Fecha de inicio de la campaña',)
    fechafin = models.DateTimeField(verbose_name='Fecha de final de la campaña',)	
    nummcctipo = models.IntegerField(verbose_name='Tipo mcc',)
    nummccestado = models.ForeignKey(MccEstado,verbose_name='Mcc Estado',)
    region = models.ForeignKey(Region, verbose_name='Region')
    provincia = models.ForeignKey(Provincia, verbose_name='Provincia')
    descripcionmcc = models.TextField(verbose_name='Breve descripción y estado actual del mcc',)
    propuestamcc = models.TextField(verbose_name='Propuesta del mcc',)
    idusuario_creac = models.IntegerField(verbose_name='Usuario creador',)
    fec_creac = models.DateTimeField(verbose_name='Fecha de creación del registro',auto_now_add=True)
    idusuario_mod = models.IntegerField(verbose_name='Usuario modifico', null=True, blank=True)
    fec_mod = models.DateTimeField(verbose_name='Fecha modifico', auto_now=True, null=True, blank=True)
    idadministrador_mod	= models.IntegerField(verbose_name='Usuario modifico', null=True, blank=True)
    fec_modadm = models.DateTimeField(verbose_name='Fecha modifico', auto_now=True, null=True, blank=True)

    class Meta:
        db_table = u'mcc'
        verbose_name = u'Matriz de Campaña de Crisis'
        verbose_name_plural = u'Matrices de Campaña de Crisis'

    def __unicode__(self):
        return self.nombremmca


class MccActor(models.Model):
    nummcc = models.ForeignKey(Mcc,verbose_name='Numero de la mcc',to_field='nummcc')
    item = models.IntegerField(verbose_name='Items',)    
    numtipovarios = models.IntegerField(verbose_name='Numero de Tipo Varios de mcc')
    actor = models.CharField(verbose_name='Actor involucrado', max_length=100)
    institucion = models.CharField(verbose_name='Institucion Actor involucrado', max_length=100)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccactor'
        verbose_name = u'Mcc Actor'
        verbose_name_plural = u'Mcc Actor'

    def __unicode__(self):
        return self.actor

class MccLider(models.Model):
    nummcc = models.ForeignKey(Mcc,verbose_name='Numero de la mcc',to_field='nummcc')
    item = models.IntegerField(verbose_name='Items',)    
    numtipovarios = models.IntegerField(verbose_name='Numero de Tipo Varios de mcc')
    lider = models.CharField(verbose_name='Actor involucrado', max_length=100)
    institucion = models.CharField(verbose_name='Institucion Actor involucrado', max_length=100)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mcclider'
        verbose_name = u'Mcc Lider'
        verbose_name_plural = u'Mcc Lideres'

    def __unicode__(self):
        return self.actor
	

class MccObservacion(models.Model):
    nummcc = models.ForeignKey(Mcc,verbose_name='Numero de la mcc',to_field='nummcc')
    item = models.IntegerField(verbose_name='Items',)    
    observacion = models.CharField(verbose_name='Observacion de OGCS', max_length=300)
    auditoria = models.IntegerField(verbose_name='Auditoria',choices=AUDITORIA)

    class Meta:
        db_table = u'mccobservacion'
        verbose_name = u'Mcc Observacion'
        verbose_name_plural = u'Mcc Observaciones'

    def __unicode__(self):
        return self.nummcc
