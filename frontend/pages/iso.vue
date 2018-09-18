<template>
<div>
    <Button style="margin-bottom: 10px" shape="circle" icon="ios-cloud-upload-outline">上传镜像</Button>
    <Table border :columns="columns" :data="data"></Table>
</div>
</template>
<script>
    export default {
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
                data: [
                        {
                          "id": 1,
                          "os_type": "Linux",
                          "name": "CentOS-7-x86_64-Minimal-1804.iso",
                          "md5": "fabdc67ff3a1674a489953effa285dfd",
                          "status_cn": "上传完成",
                          "upload_time_str": "2018-09-13 17:05:37"
                        },
                        {
                          "id": 2,
                          "os_type": "Linux",
                          "name": "archlinux-2018.08.01-x86_64.iso",
                          "md5": "112fe4369fd9de0bdeb22b84d411d018",
                          "status_cn": "上传完成",
                          "upload_time_str": "2018-09-13 17:05:38"
                        }
                ]
            }
        },
        methods: {
            remove (index) {
                this.data.splice(index, 1);
            }
        }
    }
</script>
