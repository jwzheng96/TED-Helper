<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <form id="main" v-cloak>
      <div class="bar" style="display: flex">
        <div>
          <input type="text" v-model="searchString" placeholder="输入搜索内容"/>
        </div>
        <div>
          <button v-on:click="getMsg()"> Search</button>
        </div>
      </div>
      <ul>
        <li v-for="ted in tedRecords" :key="ted.title">
          <b-card no-body class="overflow-hidden" style="max-width: 2400px;">
            <b-row no-gutters>
              <b-col md="6">
                <a v-bind:href="ted.url">
                  <b-card-img :src="ted.image" alt="Image" class="rounded-0"></b-card-img>
                </a>
              </b-col>
              <b-col md="6">
                <b-card-body>
                  <p>TED title: {{ted.name}}</p>
                  <p>TED id: {{ted.id}}</p>
                  <p>Sentence id: {{ted.sentence_id}}</p>
                  <p style="font-weight:bold">Author: {{ted.author_name}}</p>
                  <p>Searched result:
                    <b-link v-bind:href="ted.url" target="_blank">Show Full Article</b-link>
                  </p>
                  <p>{{ted.startContent}}
                    <span style="color:red">{{ted.curContent}}</span>
                    {{ted.endContent}}</p>
                </b-card-body>
              </b-col>
            </b-row>
          </b-card>
        </li>
      </ul>
    </form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      searchString: '',
      msg: 'Welcome to TED Helper!',
      tedRecords: []
    }
  },
  methods: {
    getMsg () {
      let url = '/proxy/api/v1/ted/retrieve/' + this.searchString
      this.$http.get(url).then(res => {
        this.tedRecords = res.body
        let index = 0
        // eslint-disable-next-line
        for (let ted in this.tedRecords) {
          let length = this.searchString.length
          let preIndex = this.tedRecords[index].ted_content.indexOf(this.searchString)
          let laterIndex = preIndex + length
          let startContent = ''
          let endContent = ''
          if (preIndex === 0) {
            startContent = ''
          } else {
            startContent = this.tedRecords[index].ted_content.substring(0, preIndex)
          }
          if (laterIndex >= this.tedRecords[index].ted_content.length) {
            endContent = ''
          } else {
            endContent = this.tedRecords[index].ted_content.substring(laterIndex)
          }
          this.tedRecords[index].startContent = startContent
          this.tedRecords[index].curContent = this.searchString
          this.tedRecords[index].endContent = endContent
          ted = this.tedRecords[index]
          index++
        }
      }, err => {
        console.log(err)
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  [v-cloak] {
    display: none;
  }

  * {
    margin: 0;
    padding: 0;
  }

  body {
    font: 15px/1.3 'Open Sans', sans-serif;
    color: #5e5b64;
    text-align: center;
  }

  a, a:visited {
    outline: none;
    color: #389dc1;
  }

  a:hover {
    text-decoration: none;
  }

  section, footer, header, aside, nav {
    display: block;
  }

  .bar {
    background-color: #5c9bb7;
    background-image: -webkit-linear-gradient(top, #b2b7af, #abacad);
    background-image: -moz-linear-gradient(top, #b2b7af, #b2b7af);
    background-image: linear-gradient(top, #F8F8FF, #F8F8FF);
    box-shadow: 0 1px 1px #ccc;
    border-radius: 2px;
    width: 400px;
    padding: 14px;
    margin: 45px auto 20px;
    /*position:relative;*/
  }

  .bar input {
    background: #fff no-repeat 13px 13px;
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMC1jMDYwIDYxLjEzNDc3NywgMjAxMC8wMi8xMi0xNzozMjowMCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNSBXaW5kb3dzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkU5NEY0RTlFMTA4NzExRTM5RTEzQkFBQzMyRjkyQzVBIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkU5NEY0RTlGMTA4NzExRTM5RTEzQkFBQzMyRjkyQzVBIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6RTk0RjRFOUMxMDg3MTFFMzlFMTNCQUFDMzJGOTJDNUEiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6RTk0RjRFOUQxMDg3MTFFMzlFMTNCQUFDMzJGOTJDNUEiLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4DjA/RAAABK0lEQVR42pTSQUdEURjG8dOY0TqmPkGmRcqYD9CmzZAWJRHVRIa0iFYtM6uofYaiEW2SRJtEi9YxIklp07ZkWswu0v/wnByve7vm5ee8M+85zz1jbt9Os+WiGkYdYxjCOx5wgFeXUHmtBSzpcCGa+5BJTCjEP+0nKWAT8xqe4ArPGEEVC1hHEbs2oBwdXkM7mj/JLZrad437sCGHOfUtcziutuYu2v8XUFF/4f6vMK/YgAH1HxkBYV60AR31gxkBYd6xAeF3VzMCwvzOBpypX8V4yuFRzX2d2gD/l5yjH4fYQEnzkj4fae5rJulF2sMXVrAsaTWttRFu4Osb+1jEDT71/ZveyhouTch2fINQL9hKefKjuYFfuznXWzXMTabyrvfyIV3M4vhXgAEAUMs7K0J9UJAAAAAASUVORK5CYII=);
    border: none;
    width: 170%;
    line-height: 19px;
    padding: 11px;
    border-radius: 2px;
    -webkit-box-shadow: 0 2px 8px #c4c4c4 inset;
    box-shadow: 0 2px 8px #c4c4c4 inset;
    text-align: left;
    font-size: 14px;
    font-family: inherit;
    color: #738289;
    font-weight: bold;
    outline: none;
    text-indent: 40px;
  }

  .bar button {
    margin-left: 140px;
    display: inline-block;
    padding: 10px 25px;
    font-size: 15px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color: #fff;
    background-color: #4CAF50;
    border: none;
    border-radius: 15px;
    -webkit-box-shadow: 0 9px #999;
    box-shadow: 0 9px #999;
  }

  .bar button:hover {
    background-color: #3e8e41
  }

  .bar button:active {
    background-color: #3e8e41;
    box-shadow: 0 5px #666;
    transform: translateY(4px);
  }

  ul {
    list-style: none;
    width: 1200px;
    margin: 0 auto;
    text-align: left;
  }

  ul li {
    border-bottom: 1px solid #ddd;
    padding: 10px;
    overflow: hidden;
  }

  ul li img {
    width: 256px;
    height: 144px;
    float: left;
    border: none;
  }

  ul li p {
    margin-left: 275px;
    font-weight: bold;
    padding-top: 12px;
    color: #000000;
  }

  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 0px;
  }

  a {
    color: #42b983;
  }
</style>
