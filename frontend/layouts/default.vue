<template>
  <div class="layout">
      <Layout>
          <Header>
              <Menu mode="horizontal" theme="dark" active-name="1">
                  <div class="layout-logo"></div>
                  <div class="layout-nav">
                      <Icon type="ios-navigate"></Icon>
                  </div>
              </Menu>
          </Header>
          <Content :style="{padding: '0 50px'}">
              <Breadcrumb :style="{margin: '20px 0'}">
                  <BreadcrumbItem>Home</BreadcrumbItem>
                  <BreadcrumbItem>Components</BreadcrumbItem>
                  <BreadcrumbItem>Layout</BreadcrumbItem>
              </Breadcrumb>
              <Card>
                  <div style="min-height: 200px;">
                      Content
                      <nuxt/>
                  </div>
              </Card>
          </Content>
          <Footer class="layout-footer-center">2018 &copy; lc960127@gmail.com</Footer>
      </Layout>
  </div>
</template>

<style scoped>
.layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
}
.layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
}
.layout-nav{
    width: 420px;
    margin: 0 auto;
    margin-right: 20px;
}
.layout-footer-center{
    text-align: center;
}
</style>

