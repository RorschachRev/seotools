# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Adjectiveswithpositions(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=2)
    lemma = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'adjectiveswithpositions'

class Adjpositions(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    position = models.CharField(max_length=2)
    class Meta:
        managed = False
        db_table = 'adjpositions'

class Adjpositiontypes(models.Model):
    position = models.CharField(primary_key=True, max_length=2)
    positionname = models.CharField(max_length=24)
    class Meta:
        managed = False
        db_table = 'adjpositiontypes'

class Bncconvtasks(models.Model):
    wordid = models.IntegerField()
    pos = models.CharField(max_length=1)
    freq1 = models.IntegerField(blank=True, null=True)
    range1 = models.IntegerField(blank=True, null=True)
    disp1 = models.FloatField(blank=True, null=True)
    freq2 = models.IntegerField(blank=True, null=True)
    range2 = models.IntegerField(blank=True, null=True)
    disp2 = models.FloatField(blank=True, null=True)
    ll = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bncconvtasks'

class Bncimaginfs(models.Model):
    wordid = models.IntegerField()
    pos = models.CharField(max_length=1)
    freq1 = models.IntegerField(blank=True, null=True)
    range1 = models.IntegerField(blank=True, null=True)
    disp1 = models.FloatField(blank=True, null=True)
    freq2 = models.IntegerField(blank=True, null=True)
    range2 = models.IntegerField(blank=True, null=True)
    disp2 = models.FloatField(blank=True, null=True)
    ll = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bncimaginfs'

class Bncs(models.Model):
    wordid = models.IntegerField()
    pos = models.CharField(max_length=1)
    freq = models.IntegerField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    disp = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bncs'

class Bncspwrs(models.Model):
    wordid = models.IntegerField()
    pos = models.CharField(max_length=1)
    freq1 = models.IntegerField(blank=True, null=True)
    range1 = models.IntegerField(blank=True, null=True)
    disp1 = models.FloatField(blank=True, null=True)
    freq2 = models.IntegerField(blank=True, null=True)
    range2 = models.IntegerField(blank=True, null=True)
    disp2 = models.FloatField(blank=True, null=True)
    ll = models.FloatField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bncspwrs'

class Casedwords(models.Model):
    casedwordid = models.IntegerField(primary_key=True)
    wordid = models.IntegerField()
    cased = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'casedwords'

class Dict(models.Model):
    synsetid = models.IntegerField(blank=True, null=True)
    wordid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    lemma = models.CharField(max_length=80)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField(blank=True, null=True)
    lexid = models.IntegerField(blank=True, null=True)
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    cased = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    sampleset = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'dict'

class Glfs(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    lf = models.TextField()
    text = models.TextField(blank=True)
    issub = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'glfs'

class Ilfs(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    lf = models.TextField()
    prettylf = models.TextField()
    text = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'ilfs'

class Lexdomains(models.Model):
    lexdomainid = models.IntegerField(primary_key=True)
    lexdomainname = models.CharField(max_length=32, blank=True)
    lexdomain = models.CharField(max_length=32, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'lexdomains'

class Lexlinks(models.Model):
    synset1id = models.IntegerField()
    word1id = models.IntegerField()
    synset2id = models.IntegerField()
    word2id = models.IntegerField()
    linkid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'lexlinks'

class Linktypes(models.Model):
    linkid = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=50, blank=True)
    recurses = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'linktypes'

class Morphmaps(models.Model):
    wordid = models.IntegerField()
    pos = models.CharField(max_length=1)
    morphid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'morphmaps'

class Morphology(models.Model):
    morphid = models.IntegerField()
    wordid = models.IntegerField()
    lemma = models.CharField(max_length=80)
    pos = models.CharField(max_length=1)
    morph = models.CharField(max_length=70)
    class Meta:
        managed = False
        db_table = 'morphology'

class Morphs(models.Model):
    morphid = models.IntegerField(primary_key=True)
    morph = models.CharField(unique=True, max_length=70)
    class Meta:
        managed = False
        db_table = 'morphs'

class Postypes(models.Model):
    pos = models.CharField(primary_key=True, max_length=1)
    posname = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = 'postypes'

class Samples(models.Model):
    synsetid = models.IntegerField()
    sampleid = models.IntegerField()
    sample = models.TextField()
    class Meta:
        managed = False
        db_table = 'samples'

class Samplesets(models.Model):
    synsetid = models.IntegerField()
    sampleset = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'samplesets'

class Semlinks(models.Model):
    synset1id = models.IntegerField()
    synset2id = models.IntegerField()
    linkid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'semlinks'

class Sensemaps2021(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'sensemaps2021'

class Sensemaps2130(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'sensemaps2130'

class Sensemaps3031(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'sensemaps3031'

class Senses(models.Model):
    wordid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    synsetid = models.IntegerField()
    senseid = models.IntegerField(unique=True, blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(unique=True, max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'senses'

class Senses20(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    pos = models.CharField(max_length=1)
    senseid = models.IntegerField(unique=True, blank=True, null=True)
    sensenum = models.IntegerField()
    sensekey = models.CharField(unique=True, max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'senses20'

class Senses21(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    pos = models.CharField(max_length=1)
    senseid = models.IntegerField(unique=True, blank=True, null=True)
    sensenum = models.IntegerField()
    sensekey = models.CharField(unique=True, max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'senses21'

class Senses30(models.Model):
    wordid = models.IntegerField()
    synsetid = models.IntegerField()
    pos = models.CharField(max_length=1)
    senseid = models.IntegerField(unique=True, blank=True, null=True)
    sensenum = models.IntegerField()
    sensekey = models.CharField(unique=True, max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'senses30'

class Sensesxlexlinksxsenses(models.Model):
    linkid = models.IntegerField()
    ssynsetid = models.IntegerField()
    swordid = models.IntegerField()
    ssenseid = models.IntegerField(blank=True, null=True)
    scasedwordid = models.IntegerField(blank=True, null=True)
    ssensenum = models.IntegerField()
    slexid = models.IntegerField()
    stagcount = models.IntegerField(blank=True, null=True)
    ssensekey = models.CharField(max_length=100, blank=True)
    spos = models.CharField(max_length=1)
    slexdomainid = models.IntegerField()
    sdefinition = models.TextField(blank=True)
    dsynsetid = models.IntegerField()
    dwordid = models.IntegerField()
    dsenseid = models.IntegerField(blank=True, null=True)
    dcasedwordid = models.IntegerField(blank=True, null=True)
    dsensenum = models.IntegerField()
    dlexid = models.IntegerField()
    dtagcount = models.IntegerField(blank=True, null=True)
    dsensekey = models.CharField(max_length=100, blank=True)
    dpos = models.CharField(max_length=1)
    dlexdomainid = models.IntegerField()
    ddefinition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'sensesXlexlinksXsenses'

class Sensesxsemlinksxsenses(models.Model):
    linkid = models.IntegerField()
    ssynsetid = models.IntegerField()
    swordid = models.IntegerField()
    ssenseid = models.IntegerField(blank=True, null=True)
    scasedwordid = models.IntegerField(blank=True, null=True)
    ssensenum = models.IntegerField()
    slexid = models.IntegerField()
    stagcount = models.IntegerField(blank=True, null=True)
    ssensekey = models.CharField(max_length=100, blank=True)
    spos = models.CharField(max_length=1)
    slexdomainid = models.IntegerField()
    sdefinition = models.TextField(blank=True)
    dsynsetid = models.IntegerField()
    dwordid = models.IntegerField()
    dsenseid = models.IntegerField(blank=True, null=True)
    dcasedwordid = models.IntegerField(blank=True, null=True)
    dsensenum = models.IntegerField()
    dlexid = models.IntegerField()
    dtagcount = models.IntegerField(blank=True, null=True)
    dsensekey = models.CharField(max_length=100, blank=True)
    dpos = models.CharField(max_length=1)
    dlexdomainid = models.IntegerField()
    ddefinition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'sensesXsemlinksXsenses'

class Sensesxsynsets(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    pos = models.CharField(max_length=1)
    lexdomainid = models.IntegerField()
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'sensesXsynsets'

class Sumoarg0Maps(models.Model):
    mapid = models.IntegerField()
    sumoid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoarg0maps'

class Sumoarg1Maps(models.Model):
    mapid = models.IntegerField()
    sumoid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoarg1maps'

class Sumoarg2Maps(models.Model):
    mapid = models.IntegerField()
    sumoid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoarg2maps'

class Sumoarg3Maps(models.Model):
    mapid = models.IntegerField()
    sumoid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoarg3maps'

class Sumodisjointformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumodisjointformulas'

class Sumodisjoints(models.Model):
    sumodisjoint1id = models.IntegerField()
    sumodisjoint2id = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumodisjoints'

class Sumodomainformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumodomainformulas'

class Sumofiles(models.Model):
    sumofileid = models.IntegerField(primary_key=True)
    sumofile = models.CharField(unique=True, max_length=128)
    sumoversion = models.CharField(max_length=5, blank=True)
    sumodate = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sumofiles'

class Sumoformulas(models.Model):
    formulaid = models.IntegerField(primary_key=True)
    formula = models.TextField()
    sumofileid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoformulas'

class Sumoinstanceformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoinstanceformulas'

class Sumoinstances(models.Model):
    sumoinstanceid = models.IntegerField()
    sumoclassid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumoinstances'

class Sumomaps(models.Model):
    synsetid = models.IntegerField(primary_key=True)
    sumoid = models.IntegerField()
    sumownrel = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'sumomaps'

class Sumoparsemaps(models.Model):
    mapid = models.IntegerField(primary_key=True)
    formulaid = models.IntegerField()
    sumoid = models.IntegerField()
    sumoparsetype = models.CharField(max_length=1)
    argnum = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sumoparsemaps'

class Sumopartitionformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumopartitionformulas'

class Sumorelations(models.Model):
    sumoid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumorelations'

class Sumorules(models.Model):
    formulaid = models.IntegerField()
    formula = models.TextField()
    sumofileid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumorules'

class Sumosubclasses(models.Model):
    sumoclassid = models.IntegerField()
    sumosuperclassid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumosubclasses'

class Sumosubclassformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumosubclassformulas'

class Sumosubrelationformulas(models.Model):
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumosubrelationformulas'

class Sumosubrelations(models.Model):
    sumorelationid = models.IntegerField()
    sumosuperrelationid = models.IntegerField()
    formulaid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sumosubrelations'

class Sumotermattrs(models.Model):
    sumoid = models.IntegerField()
    sumoattr = models.CharField(max_length=1)
    class Meta:
        managed = False
        db_table = 'sumotermattrs'

class Sumoterms(models.Model):
    sumoid = models.IntegerField(primary_key=True)
    sumoterm = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'sumoterms'

class Synsetmaps2031(models.Model):
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'synsetmaps2031'

class Synsetmaps2131(models.Model):
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'synsetmaps2131'

class Synsetmaps3031(models.Model):
    synsetid = models.IntegerField()
    srcsynsetid = models.IntegerField()
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'synsetmaps3031'

class Synsets(models.Model):
    synsetid = models.IntegerField(primary_key=True)
    pos = models.CharField(max_length=1)
    lexdomainid = models.IntegerField()
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'synsets'

class Synsetsxsemlinksxsynsets(models.Model):
    linkid = models.IntegerField()
    ssynsetid = models.IntegerField()
    sdefinition = models.TextField(blank=True)
    dsynsetid = models.IntegerField()
    ddefinition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'synsetsXsemlinksXsynsets'

class Verbnetframes(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    classid = models.IntegerField()
    exampleid = models.IntegerField(blank=True, null=True)
    frameid = models.IntegerField()
    subnameid = models.IntegerField()
    nameid = models.IntegerField()
    semanticsid = models.IntegerField()
    syntaxid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    framemapid = models.IntegerField()
    fquality = models.FloatField()
    number = models.CharField(max_length=16, blank=True)
    xtag = models.CharField(max_length=16, blank=True)
    syntax = models.TextField()
    semantics = models.TextField()
    framename = models.CharField(max_length=64)
    framesubname = models.CharField(max_length=64, blank=True)
    example = models.CharField(max_length=128, blank=True)
    class_field = models.CharField(db_column='class', max_length=64) # Field renamed because it was a Python reserved word.
    lemma = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'verbnetframes'

class Verbnetroles(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    classid = models.IntegerField()
    selrestrsid = models.IntegerField()
    roletypeid = models.IntegerField()
    roleid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    rolemapid = models.IntegerField()
    rquality = models.FloatField()
    roletype = models.CharField(max_length=32)
    selrestrs = models.TextField(blank=True)
    class_field = models.CharField(db_column='class', max_length=64) # Field renamed because it was a Python reserved word.
    lemma = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'verbnetroles'

class Verbnetrolesframes(models.Model):
    synsetid = models.IntegerField(blank=True, null=True)
    wordid = models.IntegerField()
    classid = models.IntegerField()
    exampleid = models.IntegerField(blank=True, null=True)
    frameid = models.IntegerField()
    subnameid = models.IntegerField()
    nameid = models.IntegerField()
    semanticsid = models.IntegerField()
    syntaxid = models.IntegerField()
    selrestrsid = models.IntegerField()
    roletypeid = models.IntegerField()
    roleid = models.IntegerField()
    rolemapid = models.IntegerField()
    rquality = models.FloatField()
    framemapid = models.IntegerField()
    fquality = models.FloatField()
    roletype = models.CharField(max_length=32)
    selrestrs = models.TextField(blank=True)
    number = models.CharField(max_length=16, blank=True)
    xtag = models.CharField(max_length=16, blank=True)
    syntax = models.TextField()
    semantics = models.TextField()
    framename = models.CharField(max_length=64)
    framesubname = models.CharField(max_length=64, blank=True)
    example = models.CharField(max_length=128, blank=True)
    class_field = models.CharField(db_column='class', max_length=64) # Field renamed because it was a Python reserved word.
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField(blank=True, null=True)
    lexid = models.IntegerField(blank=True, null=True)
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    lemma = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'verbnetrolesframes'

class Verbswithframes(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    frameid = models.IntegerField()
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    frame = models.CharField(max_length=50, blank=True)
    lemma = models.CharField(max_length=80, blank=True)
    pos = models.CharField(max_length=1, blank=True)
    lexdomainid = models.IntegerField(blank=True, null=True)
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'verbswithframes'

class Vframemaps(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    frameid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vframemaps'

class Vframes(models.Model):
    frameid = models.IntegerField(primary_key=True)
    frame = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'vframes'

class Vframesentencemaps(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    sentenceid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vframesentencemaps'

class Vframesentences(models.Model):
    sentenceid = models.IntegerField(primary_key=True)
    sentence = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'vframesentences'

class Vnclasses(models.Model):
    classid = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', unique=True, max_length=64) # Field renamed because it was a Python reserved word.
    class Meta:
        managed = False
        db_table = 'vnclasses'

class Vnclassmembers(models.Model):
    classid = models.IntegerField()
    wordid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vnclassmembers'

class Vnclassmembersenses(models.Model):
    classid = models.IntegerField()
    wordid = models.IntegerField()
    sensenum = models.IntegerField()
    synsetid = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    quality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'vnclassmembersenses'

class Vnexamplemaps(models.Model):
    frameid = models.IntegerField()
    exampleid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vnexamplemaps'

class Vnexamples(models.Model):
    exampleid = models.IntegerField(primary_key=True)
    example = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'vnexamples'

class Vnframemaps(models.Model):
    framemapid = models.IntegerField(primary_key=True)
    wordid = models.IntegerField()
    synsetid = models.IntegerField(blank=True, null=True)
    classid = models.IntegerField()
    frameid = models.IntegerField()
    fquality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'vnframemaps'

class Vnframenames(models.Model):
    nameid = models.IntegerField(primary_key=True)
    framename = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'vnframenames'

class Vnframes(models.Model):
    frameid = models.IntegerField(primary_key=True)
    number = models.CharField(max_length=16, blank=True)
    xtag = models.CharField(max_length=16, blank=True)
    nameid = models.IntegerField()
    subnameid = models.IntegerField()
    syntaxid = models.IntegerField()
    semanticsid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vnframes'

class Vnframesubnames(models.Model):
    subnameid = models.IntegerField(primary_key=True)
    framesubname = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'vnframesubnames'

class Vngroupingmaps(models.Model):
    groupingmapid = models.IntegerField(primary_key=True)
    classid = models.IntegerField()
    wordid = models.IntegerField()
    groupingid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vngroupingmaps'

class Vngroupings(models.Model):
    groupingid = models.IntegerField(primary_key=True)
    grouping = models.CharField(unique=True, max_length=64)
    class Meta:
        managed = False
        db_table = 'vngroupings'

class Vnpredicatemaps(models.Model):
    semanticsid = models.IntegerField()
    predid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vnpredicatemaps'

class Vnpredicates(models.Model):
    predid = models.IntegerField(primary_key=True)
    pred = models.CharField(unique=True, max_length=128)
    class Meta:
        managed = False
        db_table = 'vnpredicates'

class Vnrolemaps(models.Model):
    rolemapid = models.IntegerField(primary_key=True)
    wordid = models.IntegerField()
    synsetid = models.IntegerField(blank=True, null=True)
    roleid = models.IntegerField()
    classid = models.IntegerField()
    rquality = models.FloatField()
    class Meta:
        managed = False
        db_table = 'vnrolemaps'

class Vnroles(models.Model):
    roleid = models.IntegerField(primary_key=True)
    roletypeid = models.IntegerField()
    selrestrsid = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'vnroles'

class Vnroletypes(models.Model):
    roletypeid = models.IntegerField(primary_key=True)
    roletype = models.CharField(unique=True, max_length=32)
    class Meta:
        managed = False
        db_table = 'vnroletypes'

class Vnselrestrs(models.Model):
    selrestrsid = models.IntegerField(primary_key=True)
    selrestrs = models.TextField()
    class Meta:
        managed = False
        db_table = 'vnselrestrs'

class Vnselrestrtypes(models.Model):
    selrestrid = models.IntegerField(primary_key=True)
    selrestrval = models.CharField(max_length=32)
    selrestr = models.CharField(max_length=32)
    class Meta:
        managed = False
        db_table = 'vnselrestrtypes'

class Vnsemantics(models.Model):
    semanticsid = models.IntegerField(primary_key=True)
    semantics = models.TextField()
    class Meta:
        managed = False
        db_table = 'vnsemantics'

class Vnsyntaxes(models.Model):
    syntaxid = models.IntegerField(primary_key=True)
    syntax = models.TextField(unique=True)
    class Meta:
        managed = False
        db_table = 'vnsyntaxes'

class Words(models.Model):
    wordid = models.IntegerField(primary_key=True)
    lemma = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'words'

class Wordsxsenses(models.Model):
    wordid = models.IntegerField()
    lemma = models.CharField(max_length=80)
    casedwordid = models.IntegerField(blank=True, null=True)
    synsetid = models.IntegerField()
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wordsXsenses'

class Wordsxsensesxsynsets(models.Model):
    synsetid = models.IntegerField()
    wordid = models.IntegerField()
    lemma = models.CharField(max_length=80)
    casedwordid = models.IntegerField(blank=True, null=True)
    senseid = models.IntegerField(blank=True, null=True)
    sensenum = models.IntegerField()
    lexid = models.IntegerField()
    tagcount = models.IntegerField(blank=True, null=True)
    sensekey = models.CharField(max_length=100, blank=True)
    pos = models.CharField(max_length=1)
    lexdomainid = models.IntegerField()
    definition = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'wordsXsensesXsynsets'

class Xwnparselfts(models.Model):
    synsetid = models.IntegerField()
    parse = models.TextField()
    lft = models.TextField()
    parsequality = models.IntegerField(blank=True, null=True)
    lftquality = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'xwnparselfts'

class Xwnwsds(models.Model):
    synsetid = models.IntegerField()
    wsd = models.TextField()
    text = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'xwnwsds'

