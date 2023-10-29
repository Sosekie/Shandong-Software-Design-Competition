package com.example.backend.config;

import com.google.gson.Gson;
import com.qiniu.storage.BucketManager;
import com.qiniu.storage.Region;
import com.qiniu.storage.UploadManager;
import com.qiniu.util.Auth;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class QNconfig {

    @Bean
    public com.qiniu.storage.Configuration qiniuConfig(){
        //设置存储区域
        return new com.qiniu.storage.Configuration(Region.region0());
    }

    @Bean
    public UploadManager uploadManager(){
        return new UploadManager(qiniuConfig());
    }

    @Value("${qiniu.accessKey}")
    private String accessKey;

    @Value("${qiniu.secretKey}")
    private String secretKey;

    /**
     * 获取授权
     * @return
     */
    @Bean
    public Auth auth(){
        return Auth.create(accessKey,secretKey);
    }

    /**
     * 构建一个管理实例
     * @return
     */
    @Bean
    public BucketManager bucketManager(){
        return new BucketManager(auth(),qiniuConfig());
    }

    /**
     *
     * @return
     */
    @Bean
    public Gson gson(){
        return new Gson();
    }
}

