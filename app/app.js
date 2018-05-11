'use strict' ;


import Vue from 'vue'
import './noop.js'
import {} from '@/app/noop'
import UA from './mock/user.js'


const modhello = import('./noop.js')
modhello
  .then(s => console.info(s.default))
  .catch(e => console.error(e))


const app = new Vue({
    data: () => ({
        info: 'Hello, World!'
    }),
    methods: {
        new_user: function(login) {
            this.$ua.post('/user', {login: 'user1'})
              .then(resp => console.debug(resp))
              .catch(err => console.error(err))
        }
    },
    mounted: function() {
        //app.$ua = UA

        false && this.$ua.get('/timeout')
                         .then(resp => this.info = resp.data.users.join(', '))  // this for arrow fn is in outer context
                         .catch(err => {
                             if(err instanceof Error)
                                 this.info = err.code
                             else
                                 this.info = err.response && err.response.status || 'Network error'
                         })
                         //.finally(() => {})
    }
})

app.$ua = UA
app.$mount('#app')

console.info('document.getElementById("app").__vue__.$ua.get("/user/10").then(res => console.info(res.data))')
