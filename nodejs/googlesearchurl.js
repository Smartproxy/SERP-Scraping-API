const sdk = require('api')('@smartproxy/v1.0#25e7913l1ow524w');

sdk.auth('SPusername', 'SPassword');
sdk.realTimeExample({target: 'google', parse: true, url: 'https://www.google.com/search?q=history'})
  .then(res => console.log(res))
  .catch(err => console.error(err));