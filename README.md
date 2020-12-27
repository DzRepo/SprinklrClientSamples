# SprinklrClientSamples
A collection of python command line tools that use the Sprinklr Client Library
This is a work in progress, but wanted an online backup.

The SprinklrClient library located here is a bit newer than the one in the main library. The main change being Asset APIs have been tested and fixed.

I'll be pushing out an updated library soon!

Libraries in use: easysettings (for the Conf file)

Each command file uses resultprocessor.py for the command processor and output generator. This keeps individual command scripts small, and if a change is needed to the input/output processing it can be done globally very easily.

##THESE EXAMPLES ARE NOT SUPPORTED BY SPRINKLR - USE AT YOUR OWN RISK

The activate.py command will start the process of obtaining an Access token, including opening the URL to start the process. 
FetchAccessToken.py will create the Sprinklr.conf file (but isn't finished yet- uploaded soon!)

Other commands available:
CreateAsset
CustomFieldAddOption
CustomFieldDeleteOption
FetchAccessibleUsers
FetchAccountCustomFields
FetchAllDashboards
FetchArchivedCases
FetchCaseByNumber
FetchCaseComment
FetchCaseMessagesById
FetchClientProfileLists
FetchClientQueues
FetchClientUrlShortners
FetchClientUsers
FetchClients
FetchDashboardByName
FetchDashboardStream
FetchInboundCustomFields
FetchListeningStream
FetchListeningTopics
FetchMacros
FetchMediaAssetCustomFields
FetchMessageByUMId
FetchOutboundCustomFields
FetchPartnerAccountGroups
FetchPartnerAccounts
FetchPartnerCampaigns
FetchPartnerQueues
FetchPartnerUsers
FetchPermissions
FetchProfileCustomFields
FetchReportByFile
FetchResources
FetchUMPriorities
FetchUMStatuses
FetchUser
FetchUserById
FetchUserGroups
FetchWebhookTypes
SearchAssets

## Most commands require a SprinklrClient.conf file, formatted as below.

/# Configuration File Sprinklr.conf
access_token=THE_ACCESS_TOKEN
refresh_token=THE_REFRESH_TOKEN
redirect_uri=THE_EXACT_REDIRECT_URL_STORED_FOR_THE_APP_KEY
key=THE_APP_KEY
secret=THE_SECRET_KEY
