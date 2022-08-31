const sdk = require('api')('@smartproxy/v1.0#25e7913l1ow524w');

sdk.auth('SPusername', 'SPassword');
sdk.realTimeExample({target: 'google_shopping_product', query: '8129397700139936548', parse: true})
  .then(res => console.log(res))
  .catch(err => console.error(err));