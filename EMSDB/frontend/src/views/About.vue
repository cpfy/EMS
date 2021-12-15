
<template>
  <div class="home">
    <HelloWorld msg="我是亚托克斯，是世界的终结者"/>
    <div>
    </div>
  </div>
</template>


<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

<style>
.home{
  border: solid;
}
</style>