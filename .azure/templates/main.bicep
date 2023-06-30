@secure()
param githubToken string

param staticWebApp object = { 
  name: 'Calcpad.Studio'
  location: 'westeurope'
  sku: { 
    name: 'Standard'
    size: 'Standard'
  }
  branch: 'main'
  repositoryUrl: 'https://github.com/jamesbayley/Calcpad.Studio'
  stagingEnvironmentPolicy: 'Enabled'
  buildProperties: { 
    appLocation: 'projects/Calcpad.Studio.Web'
  }
}

resource swa 'Microsoft.Web/staticSites@2022-03-01' = {
  name: staticWebApp.name
  location: staticWebApp.location
  sku: staticWebApp.sku
  properties: {
    branch: staticWebApp.branch
    repositoryToken: githubToken
    repositoryUrl: staticWebApp.repositoryUrl
    stagingEnvironmentPolicy: staticWebApp.stagingEnvironmentPolicy
    buildProperties: {
      appLocation: staticWebApp.buildProperties.appLocation
      githubActionSecretNameOverride: 'AZURE_SWA_TOKEN'
      skipGithubActionWorkflowGeneration: true
    }
  }
  tags: null
}
