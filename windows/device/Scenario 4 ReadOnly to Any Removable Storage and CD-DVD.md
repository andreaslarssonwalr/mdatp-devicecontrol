# Device control policy sample: Scenario 4

Description: This is a policy {'oma_uri': {'./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData': <devicecontrol.IntuneCustomRow object at 0x000002AE23D32240>, './Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData': <devicecontrol.IntuneCustomRow object at 0x000002AE24707560>, './Vendor/MSFT/Defender/Configuration/DefaultEnforcement': <devicecontrol.IntuneCustomRow object at 0x000002AE2474FE00>, './Vendor/MSFT/Defender/Configuration/DeviceControlEnabled': <devicecontrol.IntuneCustomRow object at 0x000002AE2474FC50>}, 'web_paths': ['windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml', 'windows/device/Intune OMA-URI/Scenario 4 ReadOnly to Any Removable Storage and CD-DVD.xml'], 'rules': {'{d2193a7f-ceec-4729-a72a-fe949639db55}': <devicecontrol.PolicyRule object at 0x000002AE24706960>}, 'groups': {'{9b28fae8-72f7-4267-a1a5-685f747a7146}': <devicecontrol.Group object at 0x000002AE24593EF0>}, 'intune_ux_support': <devicecontrol.Support object at 0x000002AE2474FA40>, 'groupsXML': '<Groups>\n\t<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->\n\t\t<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>\n\t\t<MatchType>MatchAny</MatchType>\n\t\t<DescriptorIdList>\n\t\t\t<PrimaryId>RemovableMediaDevices</PrimaryId>\n\t\t\t<PrimaryId>CdRomDevices</PrimaryId>\n\t\t\t<PrimaryId>WpdDevices</PrimaryId>\n\t\t</DescriptorIdList>\n\t</Group>\n</Groups>', 'rulesXML': '<PolicyRules>\n\t<PolicyRule Id="{d2193a7f-ceec-4729-a72a-fe949639db55}" >\n\t\t<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData -->\n\t\t<Name>ReadOnly to Any Removable Storage and CdRom</Name>\n\t\t<IncludedIdList>\n\t\t\t<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>\n\t\t</IncludedIdList>\n\t\t<ExcludedIdList>\n\t\t</ExcludedIdList>\n\t\t<Entry Id="{c1adfc3e-0347-4096-88c3-6e0777b2a15b}">\n\t\t\t<Type>Deny</Type>\n\t\t\t<AccessMask>6</AccessMask>\n\t\t\t<Options>0</Options>\n\t\t</Entry>\n\t\t<Entry Id="{fee5f127-951b-4ece-9196-fa1c9ff21678}">\n\t\t\t<Type>AuditDenied</Type>\n\t\t\t<AccessMask>6</AccessMask>\n\t\t\t<Options>3</Options>\n\t\t</Entry>\n\t</PolicyRule>\n</PolicyRules>', 'mac_policy': None, 'mac_error': 'Primary ID [CdRomDevices] is not supported on macOS.', 'windows_support': <devicecontrol.Support object at 0x000002AE2474DFD0>, 'entry_type': <devicecontrol.WindowsEntryType object at 0x000002AE24590E60>, 'description': <__main__.Description object at 0x000002AE23F85D00>}              
Device Type: Windows Removable Device

A device control policy is a combination of [policy rules](#policy-rules), [groups](#groups) and [settings](#settings).  
This sample is based on the [sample files](#files).  
To configure the sample, follow the [deployment instructions](#deployment-instructions).  

## Policy Rules


<table>
    <tr>
        <th rowspan="2" valign="top">Name</th>
        <th colspan="2" valign="top"><center>Devices</center></th>
        <th rowspan="2" valign="top">Rule Type</th>
        <th colspan="6" valign="top"><center>Access</center></th>
        <th rowspan="2" valign="top">Notification</th>
        <th rowspan="2" valign="top">Conditions</th>
    </tr>
    <tr>
        <th>Included</th>
        <th>Excluded</th>
        <th>Disk Read</th>
		<th>Disk Write</th>
		<th>Disk Execute</th>
		<th>File Read</th>
		<th>File Write</th>
		<th>File Execute</th></tr><tr>
            <td rowspan="2" valign="top"><b>ReadOnly to Any Removable Storage and CdRom</b></td>
            <td rowspan="2 valign="top">
                <ul><li>Group: Any Removable Storage and CD-DVD and WPD Group_1<a href="#any-removable-storage-and-cd-dvd-and-wpd-group_1" title="MatchAny {'PrimaryId': 'WpdDevices'}"> (details)</a>  
</ul>
            </td>
            <td rowspan="2" valign="top">
                <ul></ul>
            </td>
            <td>Deny</td>
            <td>-</td>
            <td>:x:</td>
            <td>:x:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>None (0)</td> 
            <td>
                <center>-</center></td>
        </tr><tr>
            <td>Audit Denied</td>
            <td>-</td>
            <td>:page_facing_up:</td>
            <td>:page_facing_up:</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>Show notification and Send event (3)</td>
            <td> 
                <center>-</center></td>
        </tr></table>


## Groups


### Any Removable Storage and CD-DVD and WPD Group_1



This is a group of type *Device*. 
The match type for the group is *MatchAny*.


|  Property | Value |
|-----------|-------|
| PrimaryId | RemovableMediaDevices |
| PrimaryId | CdRomDevices |
| PrimaryId | WpdDevices |





<details>
<summary>View XML</summary>

```xml
<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
	<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
	<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
	<MatchType>MatchAny</MatchType>
	<DescriptorIdList>
		<PrimaryId>RemovableMediaDevices</PrimaryId>
		<PrimaryId>CdRomDevices</PrimaryId>
		<PrimaryId>WpdDevices</PrimaryId>
	</DescriptorIdList>
</Group>
```
</details>


## Settings
| Setting Name |  Setting Value | Documentation |
|--------------|----------------|---------------|
DefaultEnforcement | Deny | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdefaultenforcement) |
DeviceControlEnabled | True | [documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/defender-csp#configurationdevicecontrolenabled) |


## Files
This policy is based on information in the following files:

- [windows/device/Intune OMA-URI/Scenario 4 ReadOnly to Any Removable Storage and CD-DVD.xml](/windows/device/Intune%20OMA-URI/Scenario%204%20ReadOnly%20to%20Any%20Removable%20Storage%20and%20CD-DVD.xml)
- [windows/device/Group Policy/Any Removable Storage and CD-DVD and WPD Group.xml](/windows/device/Group%20Policy/Any%20Removable%20Storage%20and%20CD-DVD%20and%20WPD%20Group.xml)


# Deployment Instructions

Device control [policy rules](#policy-rules) and [groups](#groups) can be deployed through the following management tools:


## Windows
- [Intune UX](#intune-ux)
- [Intune Custom Settings](#intune-custom-settings)
- [Group Policy (GPO)](#group-policy-gpo)





## Intune UX

<details>
<summary>Create a reusable setting for Any Removable Storage and CD-DVD and WPD Group_1</summary> 

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on Reusable Settings
   3. Click (+) Add
   4. Enter the Any Removable Storage and CD-DVD and WPD Group_1 for the name.  
   5. Optionally, enter a description
   6. Click on "Next"
   7. Set the match type toggle to MatchAny
   
   8. Click "Next"
   9. Click "Add"
</details>
<details>
<summary>Create a Device Control Rules configuration profile</summary>  

   1. Navigate to Home > Endpoint Security > Attack Surface Reduction
   2. Click on "Create Policy"
   3. Under Platform, select "Windows 10 and later"
   4. Under Profile, select "Device Control Rules"
   5. Click "Create"
   6. Under Name, enter **
   7. Optionally, enter a description
   8. Click "Next"
</details>


<details>
<summary>Add a rule for ReadOnly to Any Removable Storage and CdRom to the policy</summary>


   1. Click on "+ Set reusable settings" under Included Id

   1. Click on *Any Removable Storage and CD-DVD and WPD Group_1*

   1. Click on "Select"


   1. Click on "+ Edit Entry"
   1. Enter *ReadOnly to Any Removable Storage and CdRom* for the name



   1. Select *Deny* from "Type"
   1. Select *None* from "Options"
   1. Select *Write and Execute* from "Access mask"




   1. Add another entry.  Click on "+ Add"

   1. Select *Audit Denied* from "Type"
   1. Select *Show notification and Send event* from "Options"
   1. Select *Write and Execute* from "Access mask"


   1. Click "OK"
</details>



## Group Policy (GPO)
<details>
<summary>Define device control policy groups</summary>

   1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy groups.
   2. Save the XML below to a network share.
```xml
<Groups>
	<Group Id="{9b28fae8-72f7-4267-a1a5-685f747a7146}" Type="Device">
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData -->
		<Name>Any Removable Storage and CD-DVD and WPD Group_1</Name>
		<MatchType>MatchAny</MatchType>
		<DescriptorIdList>
			<PrimaryId>RemovableMediaDevices</PrimaryId>
			<PrimaryId>CdRomDevices</PrimaryId>
			<PrimaryId>WpdDevices</PrimaryId>
		</DescriptorIdList>
	</Group>
</Groups>
```
   3. In the Define device control policy groups window, select *Enabled* and specify the network share file path containing the XML groups data.
</details>

<details>
<summary>Define device control policy rules</summary>
 
  1. Go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Device Control > Define device control policy rules.
  2. Save the XML below to a network share.
```xml
<PolicyRules>
	<PolicyRule Id="{d2193a7f-ceec-4729-a72a-fe949639db55}" >
		<!-- ./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData -->
		<Name>ReadOnly to Any Removable Storage and CdRom</Name>
		<IncludedIdList>
			<GroupId>{9b28fae8-72f7-4267-a1a5-685f747a7146}</GroupId>
		</IncludedIdList>
		<ExcludedIdList>
		</ExcludedIdList>
		<Entry Id="{c1adfc3e-0347-4096-88c3-6e0777b2a15b}">
			<Type>Deny</Type>
			<AccessMask>6</AccessMask>
			<Options>0</Options>
		</Entry>
		<Entry Id="{fee5f127-951b-4ece-9196-fa1c9ff21678}">
			<Type>AuditDenied</Type>
			<AccessMask>6</AccessMask>
			<Options>3</Options>
		</Entry>
	</PolicyRule>
</PolicyRules>
```
  3. In the Define device control policy rules window, select *Enabled*, and enter the network share file path containing the XML rules data.
</details>

## Intune Custom Settings

<details>
<summary>Create custom intune configuration</summary>

   1. Navigate to Devices > Configuration profiles
   2. Click Create (New Policy)
   3. Select Platform "Windows 10 and Later"
   4. Select Profile "Templates"
   5. Select Template Name "Custom"
   6. Click "Create"
   7. Under Name, enter **
   8. Optionally, enter a description
   9. Click "Next" 
</details>
<details>
<summary>Add a row for ReadOnly to Any Removable Storage and CdRom</summary>  
   
   1. Click "Add"
   2. For Name, enter *ReadOnly to Any Removable Storage and CdRom*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyRules/%7Bd2193a7f-ceec-4729-a72a-fe949639db55%7D/RuleData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Scenario 4 ReadOnly to Any Removable Storage and CD-DVD.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for Any Removable Storage and CD-DVD and WPD Group_0</summary>  
   
   1. Click "Add"
   2. For Name, enter *Any Removable Storage and CD-DVD and WPD Group_0*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControl/PolicyGroups/%7B9b28fae8-72f7-4267-a1a5-685f747a7146%7D/GroupData*
   5. For Data type, select *String (XML File)*
   
        
   6. For Custom XML, select  *windows\device\Intune OMA-URI\Any Removable Storage and CD-DVD and WPD Group.xml*
         
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for DefaultEnforcement</summary>  
   
   1. Click "Add"
   2. For Name, enter *DefaultEnforcement*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DefaultEnforcement*
   5. For Data type, select *Integer*
   
   7. For Value, enter *2*
   
   7. Click "Save"
</details>
<details>
<summary>Add a row for DeviceControlEnabled</summary>  
   
   1. Click "Add"
   2. For Name, enter *DeviceControlEnabled*
   3. For Description, enter **
   4. For OMA-URI, enter  *./Vendor/MSFT/Defender/Configuration/DeviceControlEnabled*
   5. For Data type, select *Integer*
   
   7. For Value, enter *1*
   
   7. Click "Save"
</details>


