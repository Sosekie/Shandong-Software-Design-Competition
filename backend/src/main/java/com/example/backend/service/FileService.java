package com.example.backend.service;

import com.example.backend.utils.AjaxResult;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;


public interface FileService {
    AjaxResult uploadPicture(MultipartFile file) throws IOException;

    AjaxResult deletePicture(String fileName);
}

