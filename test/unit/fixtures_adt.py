import sap.adt
from sap.adt.objects import xmlns_adtcore_ancestor

from mock import Response

OBJECT_METADATA = sap.adt.ADTCoreData(language='EN', master_language='EN', master_system='NPL', responsible='FILAK')

EMPTY_RESPONSE_OK = Response(text='', status_code=200, headers={})

LOCK_RESPONSE_OK = Response(text='<sap><LOCK_HANDLE>win</LOCK_HANDLE></sap>',
                            status_code=200,
                            headers={'Content-Type': 'dataname=com.sap.adt.lock.Result'})

DEFINITIONS_READ_RESPONSE_OK = Response(text='* definitions',
                                         status_code=200,
                                         headers={'Content-Type': 'text/plain; charset=utf-8'})

IMPLEMENTATIONS_READ_RESPONSE_OK = Response(text='* implementations',
                                         status_code=200,
                                         headers={'Content-Type': 'text/plain; charset=utf-8'})

TEST_CLASSES_READ_RESPONSE_OK = Response(text='* test classes',
                                         status_code=200,
                                         headers={'Content-Type': 'text/plain; charset=utf-8'})

TASK_NUMBER='1A2B3C4D5E'
TRANSPORT_NUMBER='E5D4C3B2A1'

TASK_RELEASE_OK_RESPONSE = f'''<?xml version="1.0" encoding="UTF-8"?>
<tm:root xmlns:tm="http://www.sap.com/cts/adt/tm" tm:useraction="newreleasejobs" tm:releasetimestamp="20190212191502 " tm:number="{TASK_NUMBER}">
  <tm:releasereports>
    <chkrun:checkReport xmlns:chkrun="http://www.sap.com/adt/checkrun" chkrun:reporter="transportrelease" chkrun:triggeringUri="/sap/bc/adt/cts/transportrequests/{TASK_NUMBER}" chkrun:status="released" chkrun:statusText="Transport request/task {TASK_NUMBER} was successfully released"/>
  </tm:releasereports>
</tm:root>'''

TRASNPORT_RELEASE_OK_RESPONSE = f'''<?xml version="1.0" encoding="UTF-8"?>
<tm:root xmlns:tm="http://www.sap.com/cts/adt/tm" tm:useraction="newreleasejobs" tm:releasetimestamp="20190212191502 " tm:number="{TRANSPORT_NUMBER}">
  <tm:releasereports>
    <chkrun:checkReport xmlns:chkrun="http://www.sap.com/adt/checkrun" chkrun:reporter="transportrelease" chkrun:triggeringUri="/sap/bc/adt/cts/transportrequests/{TRANSPORT_NUMBER}" chkrun:status="released" chkrun:statusText="Transport request/task {TRANSPORT_NUMBER} was successfully released"/>
  </tm:releasereports>
</tm:root>'''

SHORTENED_WORKBENCH_XML = f'''<?xml version="1.0" encoding="UTF-8"?>
<tm:root xmlns:tm="http://www.sap.com/cts/adt/tm" xmlns:adtcore="http://www.sap.com/adt/core">
    <tm:workbench tm:category="Workbench">
        <tm:target tm:name="/TGT/" tm:desc="Target Description">
            <tm:modifiable tm:status="Modifiable">
                <tm:request tm:number="{TRANSPORT_NUMBER}" tm:parent="" tm:owner="FILAK" tm:desc="Transport Description" tm:type="K" tm:status="D" tm:target="" tm:target_desc="" tm:cts_project="" tm:cts_project_desc="" tm:lastchanged_timestamp="20190206110506" tm:uri="/sap/bc/adt/vit/wb/object_type/%20%20%20%20rq/object_name/{TRANSPORT_NUMBER}">
                    <tm:long_desc/>
                    <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="/sap/bc/adt/cts/transportrequests/{TRANSPORT_NUMBER}" rel="http://www.sap.com/cts/relations/adturi" type="application/vnd.sap.adt.transportrequests.v1+xml" title="Transport Organizer ADT URI"/>
                    <tm:abap_object tm:pgmid="CORR" tm:type="RELE" tm:name="NPLK000006 20190216 142210 DEVELOPER" tm:obj_info="Comment Entry: Released"/>
                    <tm:task tm:number="{TASK_NUMBER}" tm:parent="{TRANSPORT_NUMBER}" tm:owner="FILAK" tm:desc="Task Description" tm:type="Development/Correction" tm:status="D" tm:target="" tm:target_desc="" tm:cts_project="" tm:cts_project_desc="" tm:lastchanged_timestamp="20190212190504" tm:uri="/sap/bc/adt/vit/wb/object_type/%20%20%20%20rq/object_name/{TASK_NUMBER}">
                        <tm:long_desc/>
                        <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="/sap/bc/adt/cts/transportrequests/{TASK_NUMBER}" rel="http://www.sap.com/cts/relations/adturi" type="application/vnd.sap.adt.transportrequests.v1+xml" title="Transport Organizer ADT URI"/>
                        <tm:abap_object tm:pgmid="LIMU" tm:type="TABD" tm:name="FOO" tm:wbtype="TABL/DS" tm:dummy_uri="/sap/bc/adt/cts/transportrequests/reference?obj_name=FOO&amp;obj_wbtype=TABD&amp;pgmid=LIMU" tm:obj_info="Table Definition" tm:obj_desc="Object Description" tm:position="000001" tm:lock_status="X" tm:img_activity="">
                                <atom:link xmlns:atom="http://www.w3.org/2005/Atom" href="/sap/bc/adt/cts/transportrequests/{TASK_NUMBER}" rel="http://www.sap.com/cts/relations/removeobject" type="application/xml" title="Transport Organizer Remove Locked Object"/>
                        </tm:abap_object>
                    </tm:task>
                </tm:request>
            </tm:modifiable>
        </tm:target>
    </tm:workbench>
</tm:root>
'''

GET_DUMMY_OBJECT_ADT_XML = '''<?xml version="1.0" encoding="utf-8"?>
<win:dummies xmlns:class="http://www.sap.com/adt/awesome/success" xmlns:adtcore="http://www.sap.com/adt/core" adtcore:responsible="DEVELOPER" adtcore:masterLanguage="EN" adtcore:masterSystem="NPL" adtcore:name="SOFTWARE_ENGINEER" adtcore:type="DUMMY/S" adtcore:changedAt="2019-03-07T20:22:01Z" adtcore:version="active" adtcore:createdAt="2019-02-02T00:00:00Z" adtcore:changedBy="DEVELOPER" adtcore:createdBy="DEVELOPER" adtcore:description="You cannot stop me!" adtcore:descriptionTextLimit="60" adtcore:language="CZ">
  <adtcore:packageRef adtcore:name='UNIVERSE'/>
</win:dummies>
'''

ERROR_XML_PACKAGE_ALREADY_EXISTS='''<?xml version="1.0" encoding="utf-8"?><exc:exception xmlns:exc="http://www.sap.com/abapxml/types/communicationframework"><namespace id="com.sap.adt"/><type id="ExceptionResourceAlreadyExists"/><message lang="EN">Resource Package $SAPCLI_TEST_ROOT does already exist.</message><localizedMessage lang="EN">Resource Package $SAPCLI_TEST_ROOT does already exist.</localizedMessage><properties/></exc:exception>'''

ERROR_XML_MADEUP_PROBLEM='''<?xml version="1.0" encoding="utf-8"?><exc:exception xmlns:exc="http://www.sap.com/abapxml/types/communicationframework"><namespace id="org.example.whatever"/><type id="UnitTestSAPCLI"/><message lang="EN">Made up problem.</message><localizedMessage lang="EN">Made up problem.</localizedMessage><properties/></exc:exception>'''


class DummyADTObject(sap.adt.ADTObject):

    OBJTYPE = sap.adt.ADTObjectType(
        'DUMMY/S',
        'awesome/success',
        xmlns_adtcore_ancestor('win', 'http://www.example.com/never/lose'),
        'application/super.cool.txt+xml',
        {'text/plain': 'no/bigdeal'},
        'dummies',
        editor_factory=sap.adt.objects.ADTObjectSourceEditor
    )

    def __init__(self, connection='noconnection', name='noobject', metadata=None):
        super(DummyADTObject, self).__init__(connection, name,
                                             metadata if metadata is not None else sap.adt.ADTCoreData(description='adt fixtures dummy object'))
