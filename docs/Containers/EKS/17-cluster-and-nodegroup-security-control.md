---
title: Cluster and Nodegroup's Security Group Control
description: The security group rules for EKS cluster and nodegroups.
subtitle: How to control cluster and nodegorup's securiy group?
---

# Cluster and Nodegroup's Security Group Control

## Using CloudFormation for Cluster and EC2 Nodegroup

=== ":simple-linux: Linux"

    ``` bash
    STACK_NAME=""
    PROJECT_NAME=""
    REGION=""

    ClusterSecurityGroup=""             # [REQUIRED] The Id of EKS Cluster Security Group.
    AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
    GeneralNodegroupSecurityGroup=""    # [REQUIRED] The Id of EKS General Nodegroup Security Group.
    BastionInstanceSecurityGroup=""     # [optional] The Id of Bastion Instance Security Group.
    VpcEndpointSecurityGroup=""         # [optional] The Id of VPC Endpoint Security Group.

    curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

    aws cloudformation deploy \
        --template-file ./security-group-rules.yaml \
        --stack-name $STACK_NAME \
        --parameter-overrides \
            ClusterSecurityGroup=$ClusterSecurityGroup \
            AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup \
            GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup \
            BastionInstanceSecurityGroup=$BastionInstanceSecurityGroup \
            VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup \
        --disable-rollback \
        --tags project=$PROJECT_NAME \
        --region $REGION
    ```

=== ":simple-windows: Windows"

    ``` powershell
    $STACK_NAME=""
    $PROJECT_NAME=""
    $REGION=""

    $ClusterSecurityGroup=""             # [REQUIRED] The Id of EKS Cluster Security Group.
    $AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
    $GeneralNodegroupSecurityGroup=""    # [REQUIRED] The Id of EKS General Nodegroup Security Group.
    $BastionInstanceSecurityGroup=""     # [optional] The Id of Bastion Instance Security Group.
    $VpcEndpointSecurityGroup=""         # [optional] The Id of VPC Endpoint Security Group.

    curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/security-group-rules.yaml

    aws cloudformation deploy `
        --template-file ./security-group-rules.yaml `
        --stack-name $STACK_NAME `
        --parameter-overrides `
            ClusterSecurityGroup=$ClusterSecurityGroup `
            AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup `
            GeneralNodegroupSecurityGroup=$GeneralNodegroupSecurityGroup `
            BastionInstanceSecurityGroup=$BastionInstanceSecurityGroup `
            VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup `
        --disable-rollback `
        --tags project=$PROJECT_NAME `
        --region $REGION
    ```

> You can use CloudFormation template [here](https://github.com/marcus16-kang/cloudformation-templates/tree/main/eks/security-group).

## Using CloudFormation for Cluster and Fargate

=== ":simple-linux: Linux"

    ``` bash
    STACK_NAME=""
    PROJECT_NAME=""
    REGION=""

    AdditionalClusterSecurityGroup=""   # [REQUIRED] The Id of EKS Additional Cluster Security Group.
    AddonNodegroupSecurityGroup=""      # [REQUIRED] The Id of EKS Add-on Nodegroup Security Group.
    FargateAppSecurityGroup=""          # [REQUIRED] The Id of Fargate App Security Group.
    VpcEndpointSecurityGroup=""         # [optional] The Id of VPC Endpoint Security Group.

    curl -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/fargate-security-group-rules.yaml

    aws cloudformation deploy \
        --template-file ./fargate-security-group-rules.yaml \
        --stack-name $STACK_NAME \
        --parameter-overrides \
            AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup \
            AddonNodegroupSecurityGroup=$AddonNodegroupSecurityGroup \
            FargateAppSecurityGroup=$FargateAppSecurityGroup \
            VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup \
        --disable-rollback \
        --tags project=$PROJECT_NAME \
        --region $REGION
    ```

=== ":simple-windows: Windows"

    ``` powershell
    $STACK_NAME=""
    $PROJECT_NAME=""
    $REGION=""

    $AdditionalClusterSecurityGroup=""  # [REQUIRED] The Id of EKS Additional Cluster Security Group.
    $AddonNodegroupSecurityGroup=""     # [REQUIRED] The Id of EKS Add-on Nodegroup Security Group.
    $FargateAppSecurityGroup=""         # [REQUIRED] The Id of Fargate App Security Group.
    $VpcEndpointSecurityGroup=""        # [optional] The Id of VPC Endpoint Security Group.

    curl.exe -LO https://raw.githubusercontent.com/marcus16-kang/cloudformation-templates/main/eks/security-group/fargate-security-group-rules.yaml

    aws cloudformation deploy `
        --template-file ./fargate-security-group-rules.yaml `
        --stack-name $STACK_NAME `
        --parameter-overrides `
            AdditionalClusterSecurityGroup=$AdditionalClusterSecurityGroup `
            AddonNodegroupSecurityGroup=$AddonNodegroupSecurityGroup `
            FargateAppSecurityGroup=$FargateAppSecurityGroup `
            VpcEndpointSecurityGroup=$VpcEndpointSecurityGroup `
        --disable-rollback `
        --tags project=$PROJECT_NAME `
        --region $REGION
    ```

## <span style="background-color: rgb(0, 51, 102);">Cluster Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ALL</td>
    <td>ALL</td>
    <td style="background-color: rgb(0, 51, 102);">Cluster Security Group</td>
    <td>Cluster Security Group (MySelf) - ALL</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(0, 51, 102);">Cluster Security Group</td>
    <td>Cluster Security Group (MySelf) - APIServer</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(0, 102, 153);">Additional Cluster Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(0, 102, 153);">Additional Cluster Security Group</td>
    <td>Additional Cluster Security Group (MySelf) - APIServer</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</td>
    <td>Nodegroup General Security Group - APIServer</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - APIServer</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>443</td>
    <td style="">Bastion Instance Security Group</td>
    <td>Bastion Instance Security Group - APIServer</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</td>
    <td>Nodegroup General Security Group - Controllers</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - Controllers</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ALL</td>
    <td>ALL</td>
    <td style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</td>
    <td>Nodegroup General Security Group (MySelf) - ALL</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(0, 102, 153);">Additional Cluster Security Group</td>
    <td>Additional Cluster Security Group - Controllers</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ALL</td>
    <td>ALL</td>
    <td style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</td>
    <td>Nodegroup General Security Group (MySelf) - ALL</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="">0.0.0.0/0</td>
    <td>Images & AWS APIs - HTTPS</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>80</td>
    <td style="">0.0.0.0/0</td>
    <td>Images & AWS APIs - HTTP</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(204, 0, 0);">Nodegroup Add-on Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>53</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - CoreDNS</td>
  </tr>
  <tr>
    <td>UDP</td>
    <td>53</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - CoreDNS</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - Controllers</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(255, 80, 80);">Nodegroup App Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Service Port</td>
    <td style="background-color: rgb(0, 51, 0);">Elastic Load Balancer Security Group</td>
    <td>Elastic Load Balancer Security Group - Application Service</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Database Port<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></td>
    <td style="background-color: rgb(102, 51, 0);">Database Security Group</td>
    <td>Database Security Group - Database</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Cache Port<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></td>
    <td style="background-color: rgb(128, 128, 0);">Cache Security Group</td>
    <td>Cache Security Group - Cache</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(204, 102, 0);">Fargate App Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ALL</td>
    <td>ALL</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group (MySelf) - ALL</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(0, 102, 153);">Additional Cluster Security Group</td>
    <td>Additional Cluster Security Group - Controllers</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>1024 - 65535</td>
    <td style="background-color: rgb(204, 0, 0);">Nodegroup Add-on Security Group</td>
    <td>Nodegroup Add-on Security Group - Controllers</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Service Port</td>
    <td style="background-color: rgb(0, 51, 0);">Elastic Load Balancer Security Group</td>
    <td>Elastic Load Balancer Security Group - Application Service</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>ALL</td>
    <td>ALL</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group (MySelf) - ALL</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>53</td>
    <td style="background-color: rgb(204, 0, 0);">Nodegroup Add-on Security Group</td>
    <td>Nodegroup Add-on Security Group - CoreDNS</td>
  </tr>
  <tr>
    <td>UDP</td>
    <td>53</td>
    <td style="background-color: rgb(204, 0, 0);">Nodegroup Add-on Security Group</td>
    <td>Nodegroup Add-on Security Group - CoreDNS</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>80</td>
    <td>0.0.0.0/0</td>
    <td>Images & AWS APIs - HTTP</td>
  </tr>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td>0.0.0.0/0</td>
    <td>Images & AWS APIs - HTTPS</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Database Port<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></td>
    <td style="background-color: rgb(102, 51, 0);">Database Security Group</td>
    <td>Database Security Group - Database</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Cache Port<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></td>
    <td style="background-color: rgb(128, 128, 0);">Cache Security Group</td>
    <td>Cache Security Group - Cache</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(51, 153, 51);">VPC Endpoint Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(153, 0, 51);">Nodegroup General Security Group</td>
    <td>Nodegroup General Security Group - AWS APIs</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>443</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group AWS APIs</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>443</td>
    <td style="">Bastion Instance Security Group</td>
    <td>Bastion Instance Security Group - AWS APIs</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
</tbody>
</table>
</tbody>
</table>

***

## <span style="background-color: rgb(0, 151, 0);">Elastic Load Balancer Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Listener Port</td>
    <td style="">0.0.0.0/0</td>
    <td>Fron Internet</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Listener Port</td>
    <td style="">CloudFront MAnaged Prefix List</td>
    <td>From CloudFront Only</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Service Port</td>
    <td style="background-color: rgb(255, 80, 80);">Nodegroup App Security Group</td>
    <td>Nodegroup App Security Group - Application Service</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Service Port</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - Application Service</td>
  </tr>
</tbody>
</table>

***

## <span style="background-color: rgb(102, 51, 0);">Database Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Database Port<sup id="fnref:1"><a class="footnote-ref" href="#fn:1">1</a></sup></td>
    <td style="background-color: rgb(255, 80, 80);">Nodegroup App Security Group</td>
    <td>Nodegroup App Security Group - Database</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Database Port</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - Database</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
</tbody>
</table>

***

## <span style="background-color: rgb(128, 128, 0);">Cache Security Group</span>

### Inbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Source</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Cache Port<sup id="fnref:2"><a class="footnote-ref" href="#fn:2">2</a></sup></td>
    <td style="background-color: rgb(255, 80, 80);">Nodegroup App Security Group</td>
    <td>Nodegroup App Security Group - Cache</td>
  </tr>
  <tr style="background-color: rgb(128, 128, 128);">
    <td>TCP</td>
    <td>Cache Port</td>
    <td style="background-color: rgb(204, 102, 0);">Fargate App Security Group</td>
    <td>Fargate App Security Group - Cache</td>
  </tr>
</tbody>
</table>

### Outbound

<table>
<thead>
  <tr>
    <th>Protocol</th>
    <th>Port</th>
    <th>Destination</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
</tbody>
</table>

[^1]:
    MySQL, MariaDB, Aurora MySQL : `3306`
    <br>
    PostgreSQL : `5432`
    <br>
    Oracle : `1521`
    <br>
    SQL Server : `1433`

[^2]:
    Redis : `6379`
    <br>
    Memcached : `11211`
