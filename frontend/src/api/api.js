  import axios from "axios"

  const API = axios.create({
    baseURL: "https://image-based-automated-and-analysis-system-production.up.railway.app"
  })

  API.interceptors.request.use((config) => {

    const token = localStorage.getItem("token")

    if(token){
      config.headers = config.headers || {}
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  })

  export default API