<template>
<div>
    <Button style="margin-bottom: 10px" shape="circle" icon="ios-cloud-upload-outline">上传镜像</Button>
    <Table border :columns="columns" :data="data"></Table>
</div>
</template>
<script>
    import axios from 'axios'
    const ISO_URL = 'http://10.66.117.2:8000/iso/'

    export default {
        asyncData ({ parmas, error }) {
          return axios({
            method: 'get',
            url: ISO_URL
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
                        title: '镜像',
                        key: 'name',
                        render: (h, params) => {
                            return h('div', [
                                h('Icon', {
                                    props: {
                                        type: 'person'
                                    }
                                }),
                                h('strong', params.row.name)
                            ]);
                        }
                    },
                    {
                        title: '系统类型',
                        key: 'os_type',
                        width: 100
                    },
                    {
                        title: 'MD5',
                        key: 'md5'
                    },
                    {
                        title: '上传时间',
                        key: 'upload_time_str'
                    },
                    {
                        title: '状态',
                        key: 'status_cn',
                        width: 100
                    },
                    {
                        title: '操作',
                        key: 'action',
                        width: 80,
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
                data: [],
                e_msg: ''
          }
        },
        methods: {
            remove (index) {
                this.data.splice(index, 1);
            }
        }
    }
</script>
