package com.example.backend.controller;

import com.example.backend.service.FileService;
import com.example.backend.utils.AjaxResult;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

/**
 * @description:
 * @author: WYG
 * @time: 2020/4/18 15:54
 */

@RestController
@RequestMapping("/file")
public class FileController {
    @Autowired
    private FileService uploadPictureService;

    @PostMapping("/upload")
    @CrossOrigin
    public AjaxResult uploadPicture(@RequestParam("file") MultipartFile multipartFile) throws IOException {
        return uploadPictureService.uploadPicture(multipartFile);
    }

    @PostMapping("/delete")
    public AjaxResult deletePicture(String fileName){
        return uploadPictureService.deletePicture(fileName);
    }


}
