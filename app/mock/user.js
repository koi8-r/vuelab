import MockAdapter from 'axios-mock-adapter'
import Axios from 'axios'


const mock = new MockAdapter(Axios, {delayResponse: 500})


const users = [
    {login: 'root'},
    {login: 'nobody'}
]


mock
  .onGet('/user', /* {params: {}} */).reply(200, users)
  .onGet(/\/user\/(\d+)/).reply(cfg => {
      //debugger ;
      const u = users[parseInt(cfg.url.replace(/.*\/(\d+)$/, '$1'))]
      return ((typeof(u) !== 'undefined') ?
              [200, u] : [404, 'User not found'])
             .concat([{'X-Engine-Version': '0.0.1'}])
  })

mock.onAny('/error').networkError()
mock.onAny('/timeout').timeout()

mock
  .onPut().reply(400, 'Not implemented')
  .onPost('/user').reply(cfg => {
      users.push(cfg.data)
      return [201, 'Created']
  })


export default Axios
