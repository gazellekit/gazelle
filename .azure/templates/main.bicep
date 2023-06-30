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
  enterpriseGradeCdnStatus: 'Disabled'
}

resource swa 'Microsoft.Web/staticSites@2022-03-01' = {
  name: staticWebApp.name
  location: staticWebApp.location
  sku: staticWebApp.sku
  properties: {
    repositoryToken: githubToken
    repositoryUrl: staticWebApp.repositoryUrl
    stagingEnvironmentPolicy: staticWebApp.stagingEnvironmentPolicy
    enterpriseGradeCdnStatus: staticWebApp.enterpriseGradeCdnStatus
    buildProperties: {
      skipGithubActionWorkflowGeneration: true
      githubActionSecretNameOverride: 'AZURE_SWA_TOKEN'
    }
  }
  tags: null
}
