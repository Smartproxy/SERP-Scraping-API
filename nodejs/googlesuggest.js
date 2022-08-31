const sdk = require('api')('@smartproxy/v1.0#25e7913l1ow524w');

sdk.auth('SPusername', 'SPassword');
sdk.realTimeExample({
  target: 'google_images',
  query: 'https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg',
  parse: false,
  geo: 'London,England,United Kingdom'
})
  .then(res => console.log(res))
  .catch(err => console.error(err));