import subprocess
import json


process=subprocess.Popen(["powershell","Get-VM | ConvertTo-Json"],stdout=subprocess.PIPE)
result=process.communicate()[0]
#print (result)
result = result.decode('utf-8')

js_obj = json.loads(str(result))
#print(js_obj)

for a in js_obj:
	print(a['VMName'])
    #for key,value in a.items():
    #    print('{} : {}'.format(key,value))



process=subprocess.Popen(["powershell","""$VMName = \"VMNAME\";$ISO=\"C:\\Users\\Administrator.DC\\Desktop\\csr1000v-universalk9.BLD_POLARIS_DEV_LATEST_20170918_080856_V16_8_0_28.iso\"
$VM = @{
  Name = $VMName 
  MemoryStartupBytes = 4GB
  Generation = 1
  NewVHDPath = \"C:\\Users\\Public\\Documents\\Hyper-V\\Virtual Hard Disks\\$VMName.vhdx\"
  NewVHDSizeBytes = 8687091200
  BootDevice = \"VHD\"
  Path = \"C:\\Virtual Machines\\$VMName\"
  SwitchName = (Get-VMSwitch).Name[0]
}
New-VM @VM
Set-VMDvdDrive -VMName \"VMNAME\" -Path $ISO"""],stdout=subprocess.PIPE)
result=process.communicate()[0]


print (result)
#result = result.decode('utf-8')

#js_obj = json.loads(str(result))
