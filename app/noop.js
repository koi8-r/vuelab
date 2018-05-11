console.log('noop module start') ;

export let a = 10 ;
export {a as z} ;
export default 11 ;

console.log('noop module end') ;
