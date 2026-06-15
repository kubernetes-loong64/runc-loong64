Name: runc
Version: %{?version}%{!?version:1}
Release: %{?release}%{!?release:1}%{?dist}
Summary: Open Container Initiative runtime (loong64)
License: Apache-2.0
URL: https://github.com/kubernetes-loong64/runc-loong64
BugURL: https://github.com/kubernetes-loong64/runc-loong64/issues
Packager: 徐晓伟 <xuxiaowei@xuxiaowei.com.cn>

# Disable strip and build-id links for cross-compiled loongarch64 binary
%global _build_id_links none
%define __strip /bin/true

%description
runc binary for the loong64 (LoongArch) architecture.

%prep
# This example has no source, so nothing here

%build
# Generate the script directly

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 runc %{buildroot}/usr/bin/runc

mkdir -p %{buildroot}/usr/share/man/man8/
install -m 644 man/runc.8 %{buildroot}/usr/share/man/man8/runc.8

mkdir -p %{buildroot}/usr/share/licenses/%{name}/
install -m 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
%license /usr/share/licenses/%{name}/LICENSE
/usr/bin/runc
/usr/share/man/man8/runc.8*

%changelog
