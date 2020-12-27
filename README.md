# SprinklrClientSamples
A collection of python command line tools that use the Sprinklr Client Library
This is a work in progress, but wanted an online backup.

The SprinklrClient library located here is a bit newer than the one in the main library. The main change being Asset APIs have been tested and fixed.

I'll be pushing out an updated library soon!

Libraries in use: easysettings (for the Conf file)

Each command file uses resultprocessor.py for the command processor and output generator. This keeps individual command scripts small, and if a change is needed to the input/output processing it can be done globally very easily.

##THESE EXAMPLES & LIBRARY ARE NOT SUPPORTED BY SPRINKLR - USE AT YOUR OWN RISK!

Please send feedback (or just let me know you're using them!) to SteveDz at Sprinklr.com

The activate.py command will start the process of obtaining an Access token, including opening the URL to start the process. 
[FetchAccessToken](FetchAccessToken.py) will create the Sprinklr.conf file (but isn't finished yet- uploaded soon!!)

Other commands available:  
[CreateAsset](CreateAsset.py)  
[CustomFieldAddOption](CustomFieldAddOption.py)  
[CustomFieldDeleteOption](CustomFieldAddOption.py)  
[FetchAccessibleUsers](FetchAccessibleUsers.py)  
[FetchAccountCustomFields](FetchAccountCustomFields.py)  
[FetchAllDashboards](FetchAllDashboards.py)  
[FetchArchivedCases](FetchArchivedCases.py)  
[FetchCaseByNumber](FetchCaseByNumber.py)  
[FetchCaseComment](FetchCaseComment.py)  
[FetchCaseMessagesById](FetchCaseMessagesById.py)  
[FetchClientProfileLists](FetchClientProfileLists.py)  
[FetchClientQueues](FetchClientQueues.py)  
[FetchClientUrlShortners](FetchClientUrlShortners.py)  
[FetchClientUsers](FetchClientUsers.py)  
[FetchClients](FetchClients.py)  
[FetchDashboardByName](FetchDashboardByName.py)  
[FetchDashboardStream](FetchDashboardStream.py)  
[FetchInboundCustomFields](FetchInboundCustomFields.py)  
[FetchListeningStream](FetchListeningStream.py)  
[FetchListeningTopics](FetchListeningTopics.py)  
[FetchMacros](FetchMacros.py)  
[FetchMediaAssetCustomFields](FetchMediaAssetCustomFields.py)  
[FetchMessageByUMId](FetchMessageByUMId.py)  
[FetchOutboundCustomFields](FetchOutboundCustomFields.py)  
[FetchPartnerAccountGroups](FetchPartnerAccountGroups.py)  
[FetchPartnerAccounts](FetchPartnerAccounts.py)  
[FetchPartnerCampaigns](FetchPartnerCampaigns.py)  
[FetchPartnerQueues](FetchPartnerQueues.py)  
[FetchPartnerUsers](FetchPartnerUsers.py)  
[FetchPermissions](FetchPermissions.py)  
[FetchProfileCustomFields](FetchProfileCustomFields.py)  
[FetchReportByFile](FetchReportByFile.py)  
[FetchResources](FetchResources.py)  
[FetchUMPriorities](FetchUMPriorities.py)  
[FetchUMStatuses](FetchUMStatuses.py)  
[FetchUser](FetchUser.py)  
[FetchUserById](FetchUserById.py)  
[FetchUserGroups](FetchUserGroups.py)  
[FetchWebhookTypes](FetchWebhookTypes.py)  
[SearchAssets](SearchAssets.py)  

## Most commands require a SprinklrClient.conf file, formatted as below. 
\#  Configuration File Sprinklr.conf  
access_token=THE_ACCESS_TOKEN   
refresh_token=THE_REFRESH_TOKEN   
redirect_uri=THE_EXACT_REDIRECT_URL_STORED_FOR_THE_APP_KEY   
key=THE_APP_KEY   
secret=THE_SECRET_KEY   
