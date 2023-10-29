package com.example.backend.service.impl;

import com.example.backend.service.FileService;
import com.example.backend.utils.AjaxResult;
import com.google.gson.Gson;
import com.qiniu.common.QiniuException;
import com.qiniu.common.Zone;
import com.qiniu.http.Response;
import com.qiniu.storage.BucketManager;
import com.qiniu.storage.Configuration;
import com.qiniu.storage.Region;
import com.qiniu.storage.UploadManager;
import com.qiniu.storage.model.DefaultPutRet;
import com.qiniu.util.Auth;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;


/**
 * @description:
 * @author: WYG
 * @time: 2020/4/18 15:46
 */
@Service
public class FileServiceImpl implements FileService {


    @Override
    public AjaxResult uploadPicture(MultipartFile file) throws IOException {
        // 获取文件名
        String fileName = file.getOriginalFilename();
        // System.out.println("上传的文件名为：" + fileName);
        // 获取文件的后缀名
        String suffixName = fileName.substring(fileName.lastIndexOf("."));
        // System.out.println("上传的后缀名为：" + suffixName);

        String qiniuUrl = "rialb9qcc.hd-bkt.clouddn.com";
        Configuration configuration = new Configuration(Region.region0());
        UploadManager uploadManager = new UploadManager(configuration);
        String accessKey = "HQ_CyIQzK7mNkjCeCU9p6fKko2EmJLT7JrjXmu_B";
        String secretKey = "yIL33KalPyknq9gcIqrbrmEyIjMfUbvn4-xDfWK2";
        String bucket = "store-butcher";
        /*FileNameMap fileNameMap = URLConnection.getFileNameMap();
        String contentTypeFor = fileNameMap.getContentTypeFor(file);
        if (contentTypeFor != null) {// 当是图片时不为空，是视频时为空
            i = 1;
        }*/
        String key = getRandomCharacterAndNumber(10) + suffixName;//生成随机文件名
        Auth auth = Auth.create(accessKey,secretKey);
        String uptoken = auth.uploadToken(bucket);
        String responseUrl = "";
        Map<String,String> res = new HashMap<>();
        try{
            byte[] localFile = file.getBytes();
            Response response = uploadManager.put(localFile,key,uptoken);
            DefaultPutRet putRet = new Gson().fromJson(response.bodyString(), DefaultPutRet.class);
            responseUrl = responseUrl + qiniuUrl + putRet.key;
            res.put("qnUrl",qiniuUrl);
            res.put("qnName",putRet.key);
            res.put("imgUrl",qiniuUrl+"/"+putRet.key);
        }catch (QiniuException e){
            Response r = e.response;
            return AjaxResult.error("文件上传失败！");
        }
        //System.out.println(responseUrl);
        return AjaxResult.success("文件上传成功！",res);
    }

    @Override
    public AjaxResult deletePicture(String fileName) {
        String accessKey = "HQ_CyIQzK7mNkjCeCU9p6fKko2EmJLT7JrjXmu_B";
        String secretKey = "yIL33KalPyknq9gcIqrbrmEyIjMfUbvn4-xDfWK2";
        String bucket = "store-butcher";
        //构造一个带指定Zone对象的配置类
        Configuration cfg = new Configuration(Zone.zone0());
        String key = fileName;
        Auth auth = Auth.create(accessKey, secretKey);
        BucketManager bucketManager = new BucketManager(auth, cfg);
        try {
            Response delete = bucketManager.delete(bucket, key);
        } catch (QiniuException ex) {
            //如果遇到异常，说明删除失败
            ex.printStackTrace();
            System.err.println(ex.code());
            System.err.println(ex.response.toString());
            return AjaxResult.error("文件删除失败！");
        }
        return AjaxResult.success("文件删除成功！");
    }

    public static String getRandomCharacterAndNumber(int length) {
        String val = "";
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            String charOrNum = random.nextInt(2) % 2 == 0 ? "char" : "num"; // 输出字母还是数字

            if ("char".equalsIgnoreCase(charOrNum)) // 字符串
            {
                int choice = random.nextInt(2) % 2 == 0 ? 65 : 97; // 取得大写字母还是小写字母
                val += (char) (choice + random.nextInt(26));
                // int choice = 97; // 指定字符串为小写字母
                val += (char) (choice + random.nextInt(26));
            } else if ("num".equalsIgnoreCase(charOrNum)) // 数字
            {
                val += String.valueOf(random.nextInt(10));
            }
        }
        return val;
    }
}

