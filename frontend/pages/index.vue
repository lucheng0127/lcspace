<template>
  <section class="container">
    <Table border :columns="columns" :data="data"></Table>
  </section>
</template>

<script>
import axios from 'axios'
const VM_URL = 'http://10.66.117.2:8000/devices/'

export default {
  asyncData ({ params, error }) {
    return axios({
      method: 'get',
     url: VM_URL
    })
    .then((res) => {
      return { data: res.data }
    })
    .catch((e) => {
      console.log(e.request)
    })
  },
  data () {
      return {
          columns: [
              {
                  title: '虚拟机',
                  key: 'name',
                  width: 150
              },
              {
                  title: 'UUID',
                  key: 'uuid'
              },
              {
                  title: '创建时间',
                  key: 'create_time_str',
                  width: 150
              },
              {
                  title: '状态',
                  key: 'status_cn',
                  width:100
              },
              {
                  title: '操作',
                  key: 'action',
                  width: 150,
                  align: 'center',
                  render: (h, params) => {
                      return h('div', [
                          h('Button', {
                              props: {
                                  type: 'error',
                                  size: 'small'
                              },
                              on: {
                                  click: () => {
                                      this.remove(params.index)
                                  }
                              }
                         }, 'Delete')
                      ]);
                  }
              }
          ],
          data: [
          ]
      }
  },
  methods: {
      remove (index) {
          this.data6.splice(index, 1);
      }
  }
}
</script>

<style>
.container {
  min-height: 76vh;
}
</style>

