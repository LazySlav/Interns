<template>
  <router-view/>
</template>

<style lang="scss">
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  font-family: Arial;
  text-decoration: none;
}
body {

  background: #EAEDF3;
}
h1 {
  color: #393F49;
  font-size: 32px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;

}
h2 {
  color: #393F49;
  font-size: 24px;
  font-style: normal;
  font-weight: 500;
  line-height: normal;
}
.center {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  min-height: 100vh;
}
.align-center {
  text-align: center;
}
.flex-center {
  display: flex;
  justify-content: center;
}
</style>
