const sdk = require('api')('@smartproxy/v1.0#25e7913l1ow524w');

sdk.auth('SPusername', 'SPassword');
sdk.realTimeExample({
  target: 'google_search',
  query: 'history',
  parse: true,
  locale: 'en-GB',
  google_results_language: 'en',
  geo: 'London,England,United Kingdom'
})
  .then(res => console.log(res))
  .catch(err => console.error(err));