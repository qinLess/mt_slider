const Koa = require('koa');
const app = new Koa();
const bodyparser = require('koa-bodyparser');
const static = require('koa-static')
const path = require('path')
const router = require('koa-router')();

const token = require('./token')
const slider = require('./slider')

// 美团商家后台登陆token加密逻辑
router.post('/token', async (ctx, next) => {
  // "https://epassport.meituan.com/api/account/login?loginContinue=http://e.waimai.meituan.com/v2/epassport/entry&&only_auth=undefined"
  let tokenData = token.Rohr_Opt.reload("https://epassport.meituan.com/api/account/login?loginContinue=http://e.waimai.meituan.com/v2/epassport/entry&&only_auth=undefined")
  ctx.response.body = tokenData
});

// 美团商家后台登陆滑块加密逻辑
router.post('/tbToken', async (ctx, next) => {
  const { request } = ctx;
  let config = request.body.data;

  config.country = '中国大陆';
  config.defaultIndex = Number(config.defaultIndex);

  for (let key in config) {
    if (config[key] === 'null') {
      config[key] = null
    }
    else if (config[key] === 'false' || config[key] === 'False') {
      config[key] = false
    }
  }

  let params = slider.get_behavior_token(config);

  ctx.response.body = params
})

app.use(bodyparser());

const staticPath = './static'
app.use(static(
  path.join(__dirname, staticPath)
))

app.use(async (ctx, next) => {
  const start = new Date();
  await next();
  const ms = new Date() - start;
  console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});

app.use(router.routes(), router.allowedMethods())

app.listen(7000);
console.log('start server ! 127.0.0.1:7000');

app.on('error', (err, ctx) => {
  console.error('server error', err, ctx)
});

module.exports = app;
