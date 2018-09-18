<template>
    <Tabs @on-click="go2uri">
        <TabPane label="虚拟机" icon="ios-laptop" name="/"></TabPane>
        <TabPane label="快照" icon="md-reverse-camera" name="/snapshot"></TabPane>
        <TabPane label="系统镜像" icon="logo-snapchat" name="/iso"></TabPane>
    </Tabs>
</template>

<script>
export default {
  methods: {
    go2uri(name) {
      this.$router.push(name)
    }
  }
}
</script>

