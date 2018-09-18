<template>
    <div>
        <Button @click="value = true" style="margin-bottom: 10px" shape="circle" icon="ios-cloud-upload-outline">上传镜像</Button>
        <Drawer
            title="上传镜像"
            v-model="value"
            width="720"
            :mask-closable="false"
            :styles="styles"
        >
           <Form :model="formData">
            </Form>
            <div class="demo-drawer-footer">
                <Button style="margin-right: 8px" @click="value = false">Cancel</Button>
                <Button type="primary" @click="value = false">Submit</Button>
            </div>
        </Drawer>    
    </div>
</template>
<script>
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
                    name: '',
                    url: '',
                    owner: '',
                    type: '',
                    approver: '',
                    date: '',
                    desc: ''
                },
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

