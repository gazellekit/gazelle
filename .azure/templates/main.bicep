param location string = resourceGroup().location
param web_app_name string

@allowed([
  'B1'
])
param sku string = 'B1'

resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: 'plan-${toLower(web_app_name)}'
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
  name: 'app-${toLower(web_app_name)}'
  location: location
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOTNETCORE|7.0'
    }
  }
}
