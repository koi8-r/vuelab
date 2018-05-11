const c = (() => {
    let counter = 0 ;
    return function() {
        return (counter += 1)
    }
})()

console.log(c())
console.log(c())
console.log(c())


const [verb, url, ...resp] = ['GET', '/', 200, {a: 'b'}]
console.info(verb, url, resp)


const hello = import('./noop.js')
hello
  .then(r => console.info(r))
  .catch(err => console.error(err))

