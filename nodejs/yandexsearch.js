const sdk = require('api')('@smartproxy/v1.0#25e7913l1ow524w');

sdk.auth('SPusername', 'SPpassword');
sdk.realTimeExample({
  target: 'yandex',
  parse: false,
  url: 'https://yandex.com/search/?text=cookies&lr=10393'
})
  .then(res => console.log(res))
  .catch(err => console.error(err));