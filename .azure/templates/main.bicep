param location string = resourceGroup().location
param webAppName string

@allowed([
  'F1'
  'B1'
])
param sku string = 'F1'

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: 'plan-${toLower(webAppName)}'
  location: location
  kind: 'linux'
  properties: {
    reserved: true
  }
  sku: {
    name: sku
  }
}

resource appService 'Microsoft.Web/sites@2020-06-01' = {
  name: 'app-${toLower(webAppName)}'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|7.0'
    }
  }
}
