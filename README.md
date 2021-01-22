# SprinklrClientSamples
A collection of python command line tools that use the Sprinklr Client Library

This is a work in progress, but in a usable state.

Built using python 3.7+

The SprinklrClient library located here is a bit newer than the one in the main library. The main change being Asset APIs have been tested and fixed.

The single "[SprinklrClientTest](https://github.com/DzRepo/SprinklrClientTest)" repo / app was getting to cumbersome, so this will replace it once all commands have been converted into individual programs.

External Libraries in use: 
- [EasySettings](https://libraries.io/pypi/EasySettings) (for the Conf file)
- [SprinklrClient](https://libraries.io/pypi/SprinklrClient) (NOTE: The version in this repo is newer than the one available via pip)
- (which uses) [Requests](https://libraries.io/pypi/requests)

Each command (except for [authorize.py](authorize.py) and [FetchAccessToken.py](FetchAccessToken.py)) uses resultprocessor.py as a standard method of making the API call and displaying results. This keeps individual command scripts small, and if a change is needed to the input/output processing it can be done globally very easily.

**THESE EXAMPLES & LIBRARY ARE NOT SUPPORTED BY SPRINKLR - USE AT YOUR OWN RISK!**

Please send feedback (or just let me know you're using them!) to SteveDz at Sprinklr.com

To use this set of examples:
- Complete the steps 1 - 3 on [Getting Started](https://developer.sprinklr.com/docs/read/api_overview/Getting_Started). 
- Use the API key and redirect URI with [authorize.py](authorize.py) to start the process of obtaining an Access token, including opening the URL in your default browser to start the process.

```python authorize.py APIKEY https://www.sprinklr.com```

> Note:
> Authorize.py requires the API key and redirect URL as set in the [Developer Portal](https://developer.sprinklr.com). Note that the Redirect URL must be *_exactly_* the same as it is listed on the portal. Optionally, if you are not generating an access token for the default Production environment (this is not typical), put in the name of the environment (like prod2 for example). If you are not sure of the environment, consult the Success Manager for your account. Note also that the API key should also match the environment. Attempting to use an API key generated for an alternate environment (QA4 for example) will return an error.

- Once complete, the redirect will be sent a code. this code is used in the next step.
- Using [FetchAccessToken](FetchAccessToken.py) with the API key, secret, code, and redirect URL (and platform if necessary).

```python FetchAccessToken.py APIKEY SECRET CODE https://www.sprinklr.com ```

- The results (Access Token, Refresh Token and the rest of the parameters) will be stored in Sprinklr.conf.  
***MAKE SURE TO SECURE THIS FILE!***

Once completed successfully, the rest of the sample applications will work. A good first one to try is [FetchUser](FetchUser.py) as it will return the user information associated with the access token. Note that all actions taken with the access token are made on behalf of the Sprinklr user account used in the Authorize step (this includes permissions, visibility of objects, etc.)

Current commands available:

* [Authorize](authorize.py)
* [CreateAsset](CreateAsset.py) 
* [CustomFieldAddOption](CustomFieldAddOption.py)  
* [CustomFieldDeleteOption](CustomFieldAddOption.py) 
* [FetchAccessibleUsers](FetchAccessibleUsers.py)  
* [FetchAccessToken](FetchAccessToken.py)
* [FetchAccountByChannelId](FetchAccountByChannelId.py)
* [FetchAccountCustomFields](FetchAccountCustomFields.py)  
* [FetchAllDashboards](FetchAllDashboards.py)  
* [FetchArchivedCases](FetchArchivedCases.py)
* [FetchAssetById](FetchAssetById.py)
* [FetchCaseByNumber](FetchCaseByNumber.py)  
* [FetchCaseComment](FetchCaseComment.py)  
* [FetchCaseMessagesById](FetchCaseMessagesById.py)  
* [FetchClientProfileLists](FetchClientProfileLists.py)  
* [FetchClientQueues](FetchClientQueues.py)  
* [FetchClientUrlShortners](FetchClientUrlShortners.py)  
* [FetchClientUsers](FetchClientUsers.py)  
* [FetchClients](FetchClients.py)  
* [FetchDashboardByName](FetchDashboardByName.py)  
* [FetchDashboardStream](FetchDashboardStream.py)  
* [FetchInboundCustomFields](FetchInboundCustomFields.py)  
* [FetchListeningStream](FetchListeningStream.py)  
* [FetchListeningTopics](FetchListeningTopics.py)  
* [FetchMacros](FetchMacros.py)  
* [FetchMediaAssetCustomFields](FetchMediaAssetCustomFields.py)  
* [FetchMessageByUMId](FetchMessageByUMId.py)  
* [FetchOutboundCustomFields](FetchOutboundCustomFields.py)  
* [FetchPartnerAccountGroups](FetchPartnerAccountGroups.py)  
* [FetchPartnerAccounts](FetchPartnerAccounts.py)  
* [FetchPartnerCampaigns](FetchPartnerCampaigns.py)  
* [FetchPartnerQueues](FetchPartnerQueues.py)  
* [FetchPartnerUsers](FetchPartnerUsers.py)  
* [FetchPermissions](FetchPermissions.py)  
* [FetchProfileCustomFields](FetchProfileCustomFields.py)  
* [FetchReportByFile](FetchReportByFile.py)  
* [FetchResources](FetchResources.py)  
* [FetchUMPriorities](FetchUMPriorities.py)  
* [FetchUMStatuses](FetchUMStatuses.py)  
* [FetchUser](FetchUser.py)  
* [FetchUserById](FetchUserById.py)  
* [FetchUserGroups](FetchUserGroups.py)  
* [FetchWebhookTypes](FetchWebhookTypes.py)  
* [SearchAssets](SearchAssets.py)
* [SendEmail](SendEmail.py)
* [UpdateAsset](UpdateAsset.py)
* [UploadAsset](UploadAsset.py)


## Format for the Sprinklr.conf file:
\#  Configuration File Sprinklr.conf  
access_token=THE_ACCESS_TOKEN   
refresh_token=THE_REFRESH_TOKEN   
redirect_uri=THE_EXACT_REDIRECT_URL_STORED_FOR_THE_APP_KEY   
key=THE_APP_KEY   
secret=THE_SECRET_KEY   
