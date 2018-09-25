<template>
    <div>
        <Button @click="value = true" style="margin-bottom: 10px" shape="circle" icon="ios-cloud-upload-outline">上传镜像</Button>
        <Drawer
            title="上传镜像"
            v-model="value"
            width="420"
            :mask-closable="false"
            :styles="styles"
        >
            <Form :model="formData">
              <Alert v-if="formData.msg" banner closable type="warning">{{ formData.msg }}</Alert>
              <Select v-model="formData.os_type" style="width:200px">
                <Option v-for="item in osList" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
              <Input v-model="formData.md5" placeholder="文件MD5" style="width: 300px" />
              <Upload
                multiple
                type="drag"
                :before-upload="handleUpload"
                :data='{os_type: this.formData.os_type, md5: this.formData.md5 }'
                action="http://10.66.117.2:8000/iso/"
                name="iso">
                <div style="padding: 20px 0">
                  <Icon type="ios-cloud-upload" size="52"></Icon>
                  <p>点击或拖拽文件至此上传</p>
                </div>
              </Upload>
            </Form>
        </Drawer>    
    </div>
</template>
<script>
    import axios from 'axios'
    const OS_TYPE_URL = 'http://10.66.117.2:8000/iso/os_type/'

    export default {
        data () {
            return {
                value: false,
                styles: {
                    height: 'calc(100% - 55px)',
                    overflow: 'auto',
                    paddingBottom: '53px',
                    position: 'static'
                },
                formData: {
                    os_type: '',
                    md5: '',
                    msg: ''
                },
                osList: [
                  {value: 'Linux', label: 'Linux'},
                  {value: 'Windows', label: 'Microsoft Windows'},
                  {value: 'BSD', label: 'BSD'},
                  {value: 'Unix', label: 'Unix'},
                  {value: 'MacOS', label: 'MacOS'},
                  {value: 'Other', label: 'Other'},
                ],
            }
        },
        methods: {
            handleUpload (file) {
                if (this.formData.md5 == '' || this.formData.os_type == '') {
                    this.formData.msg = '请选择系统类型并填写md5!'
                    return false
                }
            },
            go2 (url) {
                this.$router.push(url)
            }
        }
    }
</script>
<style>
    .demo-drawer-footer{
        width: 100%;
        position: absolute;
        bottom: 0;
        left: 0;
        border-top: 1px solid #e8e8e8;
        padding: 10px 16px;
        text-align: right;
        background: #fff;
    }
</style>

